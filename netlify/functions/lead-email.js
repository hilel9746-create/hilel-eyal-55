const RESEND_API_URL = "https://api.resend.com/emails";

// Comma-separated list of allowed origins, e.g. "https://cashbuyersohio.com,https://www.cashbuyersohio.com"
const ALLOWED_ORIGINS = (process.env.ALLOWED_ORIGINS || "")
  .split(",")
  .map((o) => o.trim())
  .filter(Boolean);

// Simple in-memory, per-IP rate limit. Survives only for the lifetime of a warm
// function instance, but meaningfully slows down scripted abuse / spam bursts.
const RATE_LIMIT_MAX = Number(process.env.RATE_LIMIT_MAX || 5); // requests
const RATE_LIMIT_WINDOW_MS = Number(process.env.RATE_LIMIT_WINDOW_MS || 60_000); // per window
const rateBuckets = new Map();

function getClientIp(event) {
  const headers = event.headers || {};
  return (
    headers["x-nf-client-connection-ip"] ||
    (headers["x-forwarded-for"] || "").split(",")[0].trim() ||
    "unknown"
  );
}

function isRateLimited(ip) {
  const now = Date.now();
  const bucket = rateBuckets.get(ip);

  if (!bucket || now > bucket.resetAt) {
    rateBuckets.set(ip, { count: 1, resetAt: now + RATE_LIMIT_WINDOW_MS });
    return false;
  }

  bucket.count += 1;
  return bucket.count > RATE_LIMIT_MAX;
}

function resolveAllowedOrigin(event) {
  const origin = (event.headers && (event.headers.origin || event.headers.Origin)) || "";
  if (ALLOWED_ORIGINS.length === 0) {
    // Not configured: fall back to same-origin only (no CORS header emitted).
    return "";
  }
  return ALLOWED_ORIGINS.includes(origin) ? origin : "";
}

function isValidEmail(value) {
  const email = String(value || "").trim();
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function isValidPhone(value) {
  const raw = String(value || "").trim();
  const normalized = raw.replace(/[^\d+]/g, "");
  const digitCount = normalized.replace(/\D/g, "").length;
  return digitCount >= 9 && digitCount <= 15;
}

function buildHeaders(allowedOrigin) {
  const headers = {
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Content-Type": "application/json",
    Vary: "Origin",
  };
  if (allowedOrigin) {
    headers["Access-Control-Allow-Origin"] = allowedOrigin;
  }
  return headers;
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function formatFieldName(key) {
  return key
    .replace(/_/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/^\w/, (char) => char.toUpperCase());
}

function buildFieldRows(data) {
  return Object.entries(data)
    .filter(([key, value]) => !["page_url", "page_path", "page_title", "submitted_at", "company_website"].includes(key) && value !== "")
    .map(([key, value]) => {
      const safeValue = Array.isArray(value) ? value.join(", ") : value;
      return `<tr><td style="padding:8px 12px;border-bottom:1px solid #e5e7eb;font-weight:600;">${escapeHtml(formatFieldName(key))}</td><td style="padding:8px 12px;border-bottom:1px solid #e5e7eb;">${escapeHtml(safeValue)}</td></tr>`;
    })
    .join("");
}

exports.handler = async (event) => {
  const allowedOrigin = resolveAllowedOrigin(event);

  if (event.httpMethod === "OPTIONS") {
    return {
      statusCode: 204,
      headers: buildHeaders(allowedOrigin),
      body: "",
    };
  }

  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      headers: buildHeaders(allowedOrigin),
      body: JSON.stringify({ ok: false, error: "Method not allowed" }),
    };
  }

  if (isRateLimited(getClientIp(event))) {
    return {
      statusCode: 429,
      headers: buildHeaders(allowedOrigin),
      body: JSON.stringify({ ok: false, error: "Too many requests. Please try again later." }),
    };
  }

  let payload;
  try {
    payload = JSON.parse(event.body || "{}");
  } catch {
    return {
      statusCode: 400,
      headers: buildHeaders(allowedOrigin),
      body: JSON.stringify({ ok: false, error: "Invalid JSON payload" }),
    };
  }

  if ((payload.company_website || "").toString().trim()) {
    return {
      statusCode: 200,
      headers: buildHeaders(allowedOrigin),
      body: JSON.stringify({ ok: true }),
    };
  }

  const apiKey = process.env.RESEND_API_KEY;
  const toEmail = process.env.LEAD_TO_EMAIL || "hilel9746@gmail.com";
  const fromEmailRaw = (process.env.FROM_EMAIL || "").trim();

  const leadName = payload.name || payload.full_name || payload.first_name || "New lead";
  const fromEmail = fromEmailRaw.includes("<")
    ? fromEmailRaw
    : `Cash Buyers Ohio <${fromEmailRaw}>`;

  if (!apiKey) {
    return {
      statusCode: 500,
      headers: buildHeaders(allowedOrigin),
      body: JSON.stringify({ ok: false, error: "Missing RESEND_API_KEY" }),
    };
  }

  if (!fromEmailRaw) {
    return {
      statusCode: 500,
      headers: buildHeaders(allowedOrigin),
      body: JSON.stringify({ ok: false, error: "Missing FROM_EMAIL" }),
    };
  }

  const emailValue = payload.email || payload.email_address || "";
  const phoneValue = payload.phone || payload.mobile || payload.phone_number || "";

  if (!isValidEmail(emailValue)) {
    return {
      statusCode: 400,
      headers: buildHeaders(allowedOrigin),
      body: JSON.stringify({ ok: false, error: "Invalid email address" }),
    };
  }

  if (!isValidPhone(phoneValue)) {
    return {
      statusCode: 400,
      headers: buildHeaders(allowedOrigin),
      body: JSON.stringify({ ok: false, error: "Invalid phone number" }),
    };
  }

  const propertyAddress = payload.property_address || "Unknown Address";
  const subject = `New Deal: ${propertyAddress} (${leadName})`;
  const rows = buildFieldRows(payload);
  
  let submittedAtFormatted = "Unknown";
  if (payload.submitted_at) {
    const d = new Date(payload.submitted_at);
    if (!isNaN(d.getTime())) {
      const mm = String(d.getMonth() + 1).padStart(2, '0');
      const dd = String(d.getDate()).padStart(2, '0');
      const yyyy = d.getFullYear();
      let hh = d.getHours();
      const min = String(d.getMinutes()).padStart(2, '0');
      const ampm = hh >= 12 ? 'PM' : 'AM';
      hh = hh % 12;
      hh = hh ? hh : 12;
      submittedAtFormatted = `${mm}/${dd}/${yyyy} ${hh}:${min} ${ampm}`;
    }
  }

  const textLines = [
    "New lead from website",
    `Name: ${payload.name || payload.full_name || payload.first_name || "N/A"}`,
    `Email: ${payload.email || "N/A"}`,
    `Phone: ${payload.phone || payload.mobile || "N/A"}`,
    `Address: ${payload.property_address || "N/A"}`,
    `Submitted at: ${submittedAtFormatted}`,
    `Page: ${payload.page_url || "N/A"}`,
    "",
    "All fields:",
    JSON.stringify(payload, null, 2),
  ];

  // Admin Email Payload
  const adminEmailBody = {
    from: fromEmail,
    to: [toEmail],
    subject,
    text: textLines.join("\n"),
    html: `
      <div style="font-family: Arial, sans-serif; color: #0f172a; line-height: 1.5;">
        <h2 style="margin:0 0 16px;">New lead from website</h2>
        <p style="margin:0 0 12px;">Submitted at: ${submittedAtFormatted}</p>
        <p style="margin:0 0 12px;">Page: ${escapeHtml(payload.page_url || "N/A")}</p>
        <table style="border-collapse:collapse;width:100%;max-width:720px;border:1px solid #e5e7eb;">
          <tbody>
            ${rows || '<tr><td style="padding:8px 12px;">No lead fields were captured.</td></tr>'}
          </tbody>
        </table>
      </div>
    `,
  };

  const requests = [];
  
  // Send to admin
  requests.push(
    fetch(RESEND_API_URL, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(adminEmailBody),
    })
  );

  // Send to seller (if email is provided)
  if (emailValue) {
    const sellerEmailBody = {
      from: fromEmail,
      to: [emailValue],
      subject: "Thank you for contacting Cash Buyers Ohio",
      html: `
        <div style="font-family: 'Inter', Arial, sans-serif; max-width: 600px; margin: 0 auto; border: 1px solid #e5e7eb; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
          <div style="background-color: #1e3a8a; padding: 32px 24px; text-align: center;">
            <h1 style="color: #ffffff; margin: 0; font-size: 24px; font-weight: 600;">Cash Buyers Ohio</h1>
          </div>
          <div style="padding: 32px 24px; background-color: #ffffff;">
            <h2 style="color: #0f172a; margin-top: 0; font-size: 20px;">Hi ${escapeHtml(leadName)},</h2>
            <p style="color: #334155; line-height: 1.6; font-size: 16px;">
              Thank you for reaching out to us! We have received your information regarding your property at <strong>${escapeHtml(payload.property_address || "your property")}</strong>.
            </p>
            <p style="color: #334155; line-height: 1.6; font-size: 16px;">
              One of our team members will review your details and get back to you shortly with a fair cash offer or tailored next steps. 
            </p>
            <p style="color: #334155; line-height: 1.6; font-size: 16px;">
              If you need immediate assistance, feel free to text or call us at <strong>+12167447725</strong>.
            </p>
            <div style="margin-top: 32px; padding-top: 24px; border-top: 1px solid #e5e7eb;">
              <p style="color: #64748b; font-size: 14px; margin: 0;">
                Best regards,<br>
                <strong>The Cash Buyers Ohio Team</strong>
              </p>
            </div>
          </div>
          <div style="background-color: #f8fafc; padding: 16px 24px; text-align: center; border-top: 1px solid #e5e7eb;">
            <p style="color: #94a3b8; font-size: 12px; margin: 0;">
              © ${new Date().getFullYear()} Cash Buyers Ohio. All rights reserved.
            </p>
          </div>
        </div>
      `,
    };

    requests.push(
      fetch(RESEND_API_URL, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${apiKey}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(sellerEmailBody),
      })
    );
  }

  const responses = await Promise.all(requests);
  const adminResponse = responses[0];
  
  if (!adminResponse.ok) {
    const result = await adminResponse.json().catch(() => ({}));
    return {
      statusCode: 500,
      headers: buildHeaders(allowedOrigin),
      body: JSON.stringify({
        ok: false,
        error: result.message || result.error || "Resend request failed",
      }),
    };
  }

  return {
    statusCode: 200,
    headers: buildHeaders(allowedOrigin),
    body: JSON.stringify({ ok: true }),
  };
};
