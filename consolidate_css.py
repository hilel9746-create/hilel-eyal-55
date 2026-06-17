import re
import os

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# We need to remove all existing @media(max-width:860px){ ... } blocks safely.
# Since we know there are exactly three, and we can visually see their contents,
# we can use a stack-based parser to remove them, or just use regex if they don't have nested media queries (which they don't).

def remove_media_blocks(css_text, marker):
    out = ""
    idx = 0
    while True:
        pos = css_text.find(marker, idx)
        if pos == -1:
            out += css_text[idx:]
            break
        # Append everything before the marker
        out += css_text[idx:pos]
        
        # Find the matching closing brace
        brace_level = 0
        start_search = css_text.find('{', pos)
        curr = start_search
        while curr < len(css_text):
            if css_text[curr] == '{':
                brace_level += 1
            elif css_text[curr] == '}':
                brace_level -= 1
                if brace_level == 0:
                    break
            curr += 1
        
        # Move idx past the closing brace
        idx = curr + 1

    return out

css_cleaned = remove_media_blocks(css, '@media(max-width:860px)')
css_cleaned = remove_media_blocks(css_cleaned, '@media (max-width: 860px)')

# Also remove the isolated .about-text-d5{order:1;} at the very bottom
css_cleaned = css_cleaned.replace('.about-text-d5{order:1;}', '')

# Remove original hamburger rules if we're redefining them, but the user said "Reuse the existing .hamburger CSS class styles already defined".
# The existing .hamburger is around line 64: 
# .hamburger { display: none; background: none; border: none; cursor: pointer; padding: 8px; }
# .hamburger span { display: block; width: 22px; height: 2px; background: var(--navy); margin: 5px 0; border-radius: 2px; transition: all .3s; }
# We will leave these alone, and just add the .open states inside the media query.

consolidated_media = """
/* ── CONSOLIDATED MOBILE STYLES (Max Width: 860px) ── */
@media(max-width:860px){
  /* Hero & Layout Layout Overrides */
  .hero-d5{grid-template-columns:1fr !important; height:auto !important; min-height:auto !important; overflow:visible !important; display: flex !important; flex-direction: column !important;}
  .hero-left-d5{padding:40px 24px !important; display:flex; flex-direction:column; justify-content:center;}
  .hero-right-d5{min-height:550px !important; position:relative !important; width:100% !important;}
  .hero-right-bg-d5{position:absolute;inset:0;display:grid;grid-template-rows:70% 30% !important;}
  .hero-left-d5 h1{font-size:2.2rem !important; margin-bottom:12px !important;}
  
  .about-d5{grid-template-columns:1fr !important; padding:60px 24px !important; gap: 10px !important;}
  .about-img-frame-d5{padding: 10px !important;}
  .about-accent-d5{display:none;}
  
  .prop-grid-d5{grid-template-columns:1fr !important;}
  
  .cta-d5{grid-template-columns:1fr !important; gap:24px !important; padding: 40px 24px !important;}
  .cta-action-d5, .cta-sub-d5{text-align:left;}
  
  .properties-d5, .process-d5{padding:20px 24px 60px 24px;}
  .divider-strip-d5{gap:28px !important; padding:18px 24px !important; justify-content:center !important;}
  .trust-row-d5{justify-content:center !important;}
  
  /* NAV D5 Mobile Overrides */
  .nav-d5 { padding: 16px 20px; }
  .n-cta { display: none; } /* Hide header CTA on mobile */
  
  /* Hamburger Menu Toggle */
  .hamburger { display: block; z-index: 101; position: relative; }
  .hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
  .hamburger.open span:nth-child(2) { opacity: 0; }
  .hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
  
  /* Mobile Dropdown Nav */
  .n-links {
    display: flex; flex-direction: column; position: absolute; top: 100%; left: 0; right: 0;
    background: rgba(255,255,255,.98); padding: 0; border-bottom: 1px solid var(--border);
    box-shadow: 0 10px 20px rgba(0,0,0,0.05); gap: 0;
    max-height: 0; overflow: hidden; opacity: 0; transition: max-height 0.4s ease, opacity 0.4s ease, padding 0.4s ease;
  }
  .n-links.open {
    max-height: 400px; opacity: 1; padding: 10px 0 20px 0;
  }
  .n-links a {
    margin: 0; padding: 16px 24px; font-size: 1.1rem; border-bottom: 1px solid #f0f0f0;
  }
  .n-links a:last-child { border-bottom: none; }
  
  /* Sticky Bottom CTA Bar */
  .mobile-bottom-cta-d5 {
    display: block !important;
    position: fixed; bottom: 0; left: 0; right: 0;
    background: #fff; padding: 16px 20px; padding-bottom: calc(16px + env(safe-area-inset-bottom));
    box-shadow: 0 -4px 20px rgba(0,0,0,0.08); z-index: 99; border-top: 1px solid #eee;
  }
  .mobile-bottom-cta-d5 .n-cta-bottom {
    display: block; width: 100%; text-align: center;
    background: var(--blue); color: #fff; padding: 16px; border-radius: 8px;
    font-weight: 700; font-size: 1.1rem; text-decoration: none;
    box-shadow: 0 4px 12px rgba(37,99,235,.2);
  }
  body {
    padding-bottom: 90px; /* Safe area so bottom CTA doesn't cover footer */
  }
}

/* Ensure bottom CTA is hidden on desktop */
.mobile-bottom-cta-d5 { display: none; }
"""

with open(file_path, 'w') as f:
    f.write(css_cleaned.strip() + "\n\n" + consolidated_media)

print("Consolidated CSS and added mobile nav/sticky CTA rules.")
