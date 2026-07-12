# SEO Keyword Expansion — Session 2026-07-12

## Context
Hillel asked whether the site would surface for searches like **"Ohio cash offers"** and similar phrases.
We generated the most logical search terms a home seller would type, audited the current keyword
coverage on the live pages, then closed the biggest gaps on `index.html`.

## Keyword audit (before)
Counted occurrences across `index.html`, `about.html`, `contact.html`, `appointment.html`:

| Term | Before | Status |
|---|---|---|
| `cash offer` | 49 | ✅ strong |
| `as-is` | 22 | ✅ strong |
| `cash home buyer` | 13 | ✅ strong |
| `inherited` | 12 | ✅ good |
| `we buy houses` | 6 | ✅ good |
| `cash buyers` | 6 | ✅ good |
| `no agent` | 9 | ✅ good |
| `sell your house fast` | 4 | ⚠️ weak |
| **`sell my house`** | **0** | ❌ gap — top search phrase, absent |
| **`no realtor`** | **0** | ❌ gap (only "no agent" existed) |
| **`avoid foreclosure`** | **0** | ❌ gap |
| **`probate`** | **0** | ❌ gap |
| **`no closing cost`** | **0** | ❌ gap |
| **city + intent** (e.g. "sell my house fast Cleveland") | **0** | ❌ biggest gap — cities were bare chips only |

## Changes made (index.html)
All edits are visible on-page content plus matching structured data. No new CSS — reused existing
`situation-card-d5`, `situation-grid-d5`, `seo-chip-grid-d5`, `faq-item-d5` classes so the design is
unchanged.

1. **Hero paragraph** — rewritten to lead with "Need to sell your house fast in Ohio?" and to include
   *no realtor* and *no closing costs*.
2. **City section** — added 4 intent-rich city cards above the existing chip list, targeting the highest-
   converting long-tail:
   - "Sell My House Fast in Cleveland"
   - "We Buy Houses in Columbus"
   - "Cash Home Buyers in Cincinnati"
   - "Sell Your House Fast in Dayton"
   The full chip list (Akron, Canton, Toledo, Youngstown, Cuyahoga/Franklin County) is kept below.
3. **Situations section** — "Inherited Property" → "Inherited & Probate Property" (adds *probate*);
   "Foreclosure Pressure" → "Avoid Foreclosure" (adds *avoid foreclosure*).
4. **FAQ** — two new items added, both mirrored into the FAQPage JSON-LD for rich-result eligibility:
   - "How do I sell my house fast in Ohio?"
   - "Can I sell my house without a realtor?"

## Keyword coverage (after, index.html)
| Term | After |
|---|---|
| `sell my house` | 5 |
| `sell your house fast` | 7 |
| `no realtor` | 4 |
| `avoid foreclosure` | 2 |
| `probate` | 2 |
| `no closing cost` | 1 |
| `sell my house fast in cleveland` | 1 |
| `we buy houses in columbus` | 1 |
| `cash home buyers in cincinnati` | 1 |

## Verification
- Both JSON-LD blocks (LocalBusiness + FAQPage) validated as parseable JSON after edits.
- Rendered page checked locally (python http.server): card order and FAQ order confirmed correct,
  design consistent with existing sections.

## Note on this commit
This commit also carries pre-existing working-tree changes made before this session
(`about.html`, `contact.html`, `assets/css/style.css`, `netlify/functions/lead-email.js` default
inbox → `hilel8978@gmail.com`, `update_site.py`). They were bundled into the same deploy.

## Follow-up ideas (not done)
- Dedicated per-city landing pages (Cleveland/Columbus/Cincinnati) for deeper local ranking.
- Mirror the "sell my house fast" phrasing into `about.html` / `contact.html` H1s.
