(function () {
  const ENDPOINT = "/.netlify/functions/lead-email";
  const FORM_SELECTOR = "form#_builder-form, form.form-YlR92G2-kE, form[data-lead-form]";
  const processedForms = new WeakSet();

  function isElement(node) {
    return node && node.nodeType === Node.ELEMENT_NODE;
  }

  function normalizeKey(element) {
    return (
      element.getAttribute("name") ||
      element.id ||
      element.getAttribute("aria-label") ||
      element.placeholder ||
      ""
    )
      .trim()
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "_")
      .replace(/^_+|_+$/g, "");
  }

  function getValue(element) {
    if (element.type === "checkbox") {
      return element.checked ? element.value || "yes" : "";
    }

    if (element.type === "radio") {
      return element.checked ? element.value : "";
    }

    if (element.tagName === "SELECT" && element.multiple) {
      return Array.from(element.selectedOptions)
        .map((option) => option.value)
        .filter(Boolean)
        .join(", ");
    }

    return (element.value || "").trim();
  }

  function collectPayload(form) {
    const payload = {};

    Array.from(form.elements).forEach((element) => {
      if (!element || !("value" in element)) return;
      if (element.disabled) return;

      const key = normalizeKey(element);
      if (!key) return;

      const value = getValue(element);
      if (value === "") return;

      if (payload[key] === undefined) {
        payload[key] = value;
        return;
      }

      if (Array.isArray(payload[key])) {
        payload[key].push(value);
        return;
      }

      payload[key] = [payload[key], value];
    });

    payload.page_url = window.location.href;
    payload.page_path = window.location.pathname;
    payload.page_title = document.title;
    payload.submitted_at = new Date().toISOString();

    return payload;
  }

  function ensureStatusElement(form) {
    let status = form.querySelector("[data-lead-form-status]");
    if (status) return status;

    status = document.createElement("div");
    status.setAttribute("data-lead-form-status", "true");
    status.setAttribute("aria-live", "polite");
    status.style.marginTop = "12px";
    status.style.fontSize = "14px";
    status.style.lineHeight = "1.4";
    status.style.minHeight = "20px";
    status.style.color = "#0f172a";

    const button = form.querySelector('button[type="submit"], input[type="submit"]');
    if (button && button.parentNode) {
      button.parentNode.insertBefore(status, button.nextSibling);
    } else {
      form.appendChild(status);
    }

    return status;
  }

  function setStatus(form, message, kind) {
    const status = ensureStatusElement(form);
    status.textContent = message;
    status.style.color = kind === "error" ? "#b42318" : "#067647";
  }

  function ensureHoneypot(form) {
    if (form.querySelector('input[name="company_website"]')) return;

    const honeypot = document.createElement("input");
    honeypot.type = "text";
    honeypot.name = "company_website";
    honeypot.autocomplete = "off";
    honeypot.tabIndex = -1;
    honeypot.setAttribute("aria-hidden", "true");
    honeypot.style.position = "absolute";
    honeypot.style.left = "-9999px";
    honeypot.style.width = "1px";
    honeypot.style.height = "1px";
    honeypot.style.opacity = "0";
    honeypot.style.pointerEvents = "none";

    form.appendChild(honeypot);
  }

  function validateEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(value || "").trim());
  }

  function validatePhone(value) {
    const normalized = String(value || "")
      .trim()
      .replace(/[^\d+]/g, "");
    const digits = normalized.replace(/\D/g, "").length;
    return digits >= 9 && digits <= 15;
  }

  function validatePayload(payload) {
    const email = payload.email || payload.email_address || "";
    const phone = payload.phone || payload.mobile || payload.phone_number || "";

    if (!validateEmail(email)) {
      return "Please enter a valid email address.";
    }

    if (!validatePhone(phone)) {
      return "Please enter a valid phone number.";
    }

    return "";
  }

  async function handleSubmit(event) {
    const form = event.target;
    if (!isElement(form)) return;
    if (!form.matches(FORM_SELECTOR)) return;

    event.preventDefault();
    event.stopImmediatePropagation();

    const submitButton = form.querySelector('button[type="submit"], input[type="submit"]');
    const previousLabel = submitButton && "value" in submitButton ? submitButton.value : "";
    const previousText = submitButton ? submitButton.textContent : "";

    const payload = collectPayload(form);
    const validationError = validatePayload(payload);

    if (payload.company_website) {
      setStatus(form, "Thanks. Your request was received.", "success");
      return;
    }

    if (validationError) {
      setStatus(form, validationError, "error");
      return;
    }

    try {
      if (submitButton) {
        submitButton.disabled = true;
        if ("value" in submitButton) submitButton.value = "Sending...";
        submitButton.textContent = "Sending...";
      }

      setStatus(form, "Sending your lead...", "success");

      const response = await fetch(ENDPOINT, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok || !data.ok) {
        throw new Error(data.error || "Unable to send the lead.");
      }

      form.reset();
      setStatus(form, "Thanks. Your request was sent successfully.", "success");
    } catch (error) {
      setStatus(form, "There was a problem sending the form. Please try again.", "error");
    } finally {
      if (submitButton) {
        submitButton.disabled = false;
        if ("value" in submitButton) submitButton.value = previousLabel;
        submitButton.textContent = previousText || submitButton.textContent;
      }
    }
  }

  function bindForm(form) {
    if (!isElement(form) || processedForms.has(form)) return;
    processedForms.add(form);
    ensureHoneypot(form);
    form.addEventListener("submit", handleSubmit, true);
  }

  function scan() {
    document.querySelectorAll(FORM_SELECTOR).forEach(bindForm);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", scan, { once: true });
  } else {
    scan();
  }

  const observer = new MutationObserver(scan);
  observer.observe(document.documentElement, { childList: true, subtree: true });
})();
