# Security Review & Hardening — Cash Buyers Ohio

**Date:** 2026-06-15
**Site:** Static site on Netlify (HTML + Netlify Functions + Edge Functions)
**Reviewer:** Claude Code (requested by Itay)

---

## Scope reviewed

- All HTML pages (`index`, `home`, `about`, `contact`, `appointment`, legal pages, `Calculator.html`)
- Netlify serverless function: `netlify/functions/lead-email.js`
- Netlify edge function: `netlify/edge-functions/calculator-auth.js`
- Client lead form: `assets/js/lead-form-submit.js`
- Config: `netlify.toml`, `.gitignore`
- Git history scan for committed secrets

---

## ✅ Already secure (no change needed)

- **No secrets in git** — `.env` and `.netlify` are gitignored; `git ls-files` confirmed nothing sensitive is tracked.
- **Calculator auth** uses SHA-256 with a salt and constant-time comparison (`calculator-auth.js`).
- **HTML escaping** applied consistently: `escapeHtml` in the email function, `escHtml` throughout the calculator print report.
- **Hash import** (`#d=...base64`) writes only to `el.value`, never to `innerHTML` → no XSS there.
- Honeypot field (`company_website`) present against basic bots.

---

## 🔧 Findings fixed (2026-06-15)

### 1. Email endpoint abuse / spam — HIGH — `netlify/functions/lead-email.js`
**Problem:** `Access-Control-Allow-Origin: *` + no rate limiting. Anyone could script
the endpoint to flood the inbox, burn the Resend quota (cost), and send mail "from"
the domain to arbitrary addresses (reputation / blacklisting risk).

**Fix:**
- Added per-IP in-memory rate limit (default 5 req / 60s → `429`). Tunable via
  `RATE_LIMIT_MAX` / `RATE_LIMIT_WINDOW_MS`.
- Restricted CORS to an allowlist via `ALLOWED_ORIGINS` env var (comma-separated).
  When unset, no CORS header is emitted (same-origin only).
- Added `Vary: Origin`.

**Action still required:** set `ALLOWED_ORIGINS` in Netlify env, e.g.
`https://cashbuyersohio.com,https://www.cashbuyersohio.com`.

### 2. Missing security headers — MEDIUM — `netlify.toml`
**Problem:** no CSP, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`,
or HSTS → clickjacking exposure and no defense-in-depth against future XSS.

**Fix:** added a `[[headers]]` block for `/*` with `X-Frame-Options: DENY`,
`X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Strict-Transport-Security`,
`Permissions-Policy`, and a **Report-Only** CSP (so inline calculator JS keeps working).

**Action still required:** after verifying no CSP violation reports, rename
`Content-Security-Policy-Report-Only` → `Content-Security-Policy` to enforce.

### 3. Unescaped `<img src>` in calculator — LOW (self-XSS) — `Calculator.html`
**Problem:** `renderPhotos` interpolated the uploaded photo value directly into an
HTML string (`src="${s}"`). Self-XSS today, but a real issue if reports are ever shared.

**Fix:** rewrote `renderPhotos` using DOM APIs (`createElement`, `img.src=`,
`addEventListener`) — no string interpolation into HTML.

### 4. Calculator caching hardening — LOW — `netlify/edge-functions/calculator-auth.js`
**Fix:** authenticated response now sets `Cache-Control: private, no-store` so the
protected page isn't stored by shared/CDN caches.

---

## 🔧 Round 2 findings fixed (2026-06-15)

### 5. Public exposure of internal files — MEDIUM — `netlify.toml`
**Problem:** `publish = "."` serves the entire repo root, so `docs/` (internal feedback,
the Netlify CLI output, **this security report**) and `scripts/` (Python) were publicly
downloadable at `cashbuyersohio.net/docs/...`.

**Fix:** added `[[redirects]]` rules returning `404` for `/docs/*` and `/scripts/*`.

### 6. Unescaped attribute interpolation in comps table — LOW (self-XSS) — `Calculator.html`
**Problem:** `addComp` interpolated values into `value="..."` attributes without escaping
(currently only ever called with empty args, so theoretical today).

**Fix:** wrapped each interpolated value in `escHtml(...)`.

### 7. `target="_blank"` without `rel` — LOW — `Calculator.html`
**Fix:** added `rel="noopener noreferrer"` to the maps/street/zillow address links.

### Also verified clean (no action needed)
- `onAddr` builds external hrefs with `encodeURIComponent` + hardcoded `https://`
  prefix → no `javascript:` scheme injection.
- Python scripts (`fix_logo.py`, `generate_legal_page.py`) only read/write local files —
  no `eval`, `subprocess`, `os.system`, or network calls.
- Only external dependency is Google Fonts (benign); CSP updated to allow it
  (`fonts.googleapis.com` / `fonts.gstatic.com`) so enforcement won't break styling.
- No `eval` / `new Function` / string-based timers in any HTML.
- `report.innerHTML` and all dynamic report rendering already use `escHtml`.

## 📌 Open follow-ups (not yet done)

1. Set `ALLOWED_ORIGINS` env var in Netlify (required for #1).
2. Flip CSP from Report-Only to enforced after validation (#2).
3. Consider Cloudflare Turnstile / reCAPTCHA on the lead form — the in-memory
   rate limit resets when the function goes cold, so it's not a hard guarantee.
4. Basic Auth on the calculator is a single shared credential — consider periodic
   rotation; fine for current single-user use.

---

## Verification

- `node -c netlify/functions/lead-email.js` → OK
- `node --check` (ESM) on `calculator-auth.js` → OK
- `renderPhotos` body parsed standalone → OK
