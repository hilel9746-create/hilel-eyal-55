# SEO Implementation — Cash Buyers Ohio (Hilel 1 LLC)

**Date:** 2026-06-14
**Site:** https://cashbuyersohio.net (static site, hosted on Netlify)
**Business:** Hilel 1 LLC — direct cash home buyer in Ohio
**Key details used:** Phone (216) 744-7725 · Email hilel8978@gmail.com · Area served: Ohio

---

## Starting point (before)

The site was effectively invisible to search engines:

- Homepage title was a default placeholder: *"Top Services & Why Choose Us"*.
- Author meta read *"Your Business Name"* (unreplaced placeholder).
- `robots.txt` existed but was **empty**.
- **No** `sitemap.xml`.
- **No** structured data (no business/location signals for Google).
- No social-sharing (Open Graph) tags.

---

## What was implemented

### 1. Per-page titles & meta descriptions (English, Ohio cash-buyer focus)
Rewrote `<title>` and `<meta name="description">` for all 6 public pages:

| Page | New title |
|------|-----------|
| index.html | Sell Your House Fast for Cash in Ohio \| Hilel 1 LLC |
| about.html | About Hilel 1 LLC \| Trusted Cash Home Buyers in Ohio |
| contact.html | Contact Us \| Get a Cash Offer for Your Ohio Home — Hilel 1 LLC |
| appointment.html | Book a Call \| Get Your Cash Offer in 24 Hours — Hilel 1 LLC |
| privacy-policy.html | Privacy Policy \| Hilel 1 LLC — Cash Buyers Ohio |
| terms-and-conditions.html | Terms & Conditions \| Hilel 1 LLC — Cash Buyers Ohio |

### 2. Replaced placeholder business data
Author meta and on-page references now use the real business name (**Hilel 1 LLC**), area (**Ohio**), and phone (**216-744-7725**).

### 3. Structured data (Local SEO)
Added `RealEstateAgent` JSON-LD to the homepage (`index.html`): name, area served (Ohio), telephone, email, logo, image. Validated as valid JSON.

### 4. Open Graph / Twitter cards
Added social-sharing tags (title, description, image, url) to index, about, contact, and appointment pages — clean previews when links are shared.

### 5. Canonical tags
Every page declares its canonical URL to prevent duplicate-content confusion.

### 6. Crawl control
- **robots.txt** — filled in; allows crawling, points to the sitemap, and blocks `/Calculator*` and `/home.html`.
- **sitemap.xml** — created, listing the 6 public pages with priorities.
- **home.html** — duplicate of homepage; set to `noindex` + canonical → `/`.
- **Calculator.html** — added `noindex, nofollow` (auth-protected internal tool).

### 7. On-page audit (verified, no changes needed)
All pages already had exactly one `<h1>` and full `alt` text on every image.

---

## Files changed
- `index.html`, `home.html`, `about.html`, `contact.html`, `appointment.html`, `privacy-policy.html`, `terms-and-conditions.html`, `Calculator.html`
- `robots.txt` (filled), `sitemap.xml` (new)

---

## Follow-up actions

### Action 1 — Fix the placeholder secondary phone number
**Where:** `contact.html:74`
**Status:** Open — needs a decision from the owner.
Currently shows a fake number: `+1 (000) 000-0000` linked to `tel:+10000000000`, marked *"(to be updated)"*. Left in place because no real secondary number was available.
**To do:** Provide a real secondary phone number to insert, **or** confirm the line should be deleted entirely.

### Action 2 — Connect Google Search Console
**Status:** Open — owner action required (cannot be done from code).
1. Go to https://search.google.com/search-console
2. Add the domain `cashbuyersohio.net` and complete verification.
3. Submit the sitemap: `https://cashbuyersohio.net/sitemap.xml`
4. Use the dashboard to monitor impressions, clicks, and search queries.

> Note: both items above are pending. Everything else is done, verified, and ready to deploy to Netlify.
