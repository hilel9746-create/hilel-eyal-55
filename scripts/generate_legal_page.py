from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent

def clean_text_to_html(input_file, output_file, title):
    with open(input_file, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Try to find the text container. Usually it's in a specific column or we can just grab text nodes.
    # We will just grab text blocks that are reasonably long.
    paragraphs = []
    for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']):
        text = p.get_text(strip=True)
        if text and len(text) > 5 and "Copyright 2026" not in text and "hilel8978@gmail" not in text and "Home" not in text and "Privacy Policy" not in text and "Terms" not in text and "Contact" not in text and "Book a Call" not in text:
            if p.name.startswith('h'):
                paragraphs.append(f"<h2>{text}</h2>")
            elif p.name == 'li':
                paragraphs.append(f"<li>{text}</li>")
            else:
                paragraphs.append(f"<p>{text}</p>")

    # Deduplicate keeping order
    seen = set()
    deduped = []
    for p in paragraphs:
        if p not in seen:
            seen.add(p)
            deduped.append(p)
            
    # Wrap lis in ul
    final_content = ""
    in_ul = False
    for p in deduped:
        if p.startswith('<li>'):
            if not in_ul:
                final_content += "<ul>\n"
                in_ul = True
            final_content += p + "\n"
        else:
            if in_ul:
                final_content += "</ul>\n"
                in_ul = False
            final_content += p + "\n"
    if in_ul:
        final_content += "</ul>\n"

    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Hillel's Team</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<!-- ══ NAV ══ -->
<nav>
  <div class="nav-inner">
    <a href="index.html" style="display:block;">
      <img src="assets/images/hillel_home_logo.png?v=home-yellow-2" alt="Home logo" class="nav-logo-img">
    </a>
    <div class="nav-links" id="nav-links">
      <a href="index.html" class="hide-mob">Home</a>
      <a href="about.html" class="hide-mob">About</a>
      <a href="contact.html" class="hide-mob">Contact</a>
      <a href="appointment.html" class="nav-cta">Book a Call</a>
    </div>
    <button class="hamburger" id="hamburger" aria-label="Toggle navigation">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>

<!-- ══ PAGE HEADER ══ -->
<header class="page-header" style="padding-bottom: 40px;">
  <h1 class="page-header-title">{title}</h1>
</header>

<!-- ══ CONTENT ══ -->
<main class="content-block">
  <div class="content-inner">
    {final_content}
  </div>
</main>

<!-- ══ FOOTER ══ -->
<footer id="footer">
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <h3>Hillel's Team</h3>
        <div class="footer-contact">
          <p><strong style="color:rgba(255,255,255,.7);">Email</strong>: <a href="mailto:hilel8978@gmail.com">hilel8978@gmail.com</a></p>
        </div>
      </div>
      <div class="footer-links">
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="contact.html">Contact</a>
        <a href="appointment.html">Book a Call</a>
        <a href="privacy-policy.html">Privacy Policy</a>
        <a href="terms-and-conditions.html">Terms Conditions</a>
      </div>
    </div>
    <div class="footer-legal">
      <p>Copyright 2026. All rights reserved</p>
      <p>Hillel's Team</p>
    </div>
  </div>
</footer>

<script>
  document.getElementById('hamburger').addEventListener('click', function() {{
    document.getElementById('nav-links').classList.toggle('active');
  }});
</script>

</body>
</html>"""

    with open(output_file, 'w') as f:
        f.write(template)

clean_text_to_html(ROOT / 'privacy-policy.html', ROOT / 'privacy-policy.html', 'Privacy Policy')
clean_text_to_html(ROOT / 'terms-and-conditions.html', ROOT / 'terms-and-conditions.html', 'Terms & Conditions')
