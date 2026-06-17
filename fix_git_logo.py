import re

html_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/index.html'
css_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(html_path, 'r') as f:
    html = f.read()

# Change the image to the one used in git body (hillel_logo_clean.png)
html = html.replace('assets/images/hillel_home_logo.png', 'assets/images/hillel_logo_clean.png')

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'r') as f:
    css = f.read()

# Make the logo style exactly like it was in git (.services-img)
css = re.sub(r'\.about-img-frame-d5 img\{[^\}]+\}', '.about-img-frame-d5 img{width:100%;max-width:220px;height:auto;object-fit:contain;object-position:center;opacity:0.7;margin:0 auto;display:block;}', css)

# Make the image appear on the right side like in git
# Original .about-d5 is grid-template-columns: 1fr 1fr (or similar, actually it's grid-template-columns: 45% 1fr or 400px 1fr)
css = re.sub(r'\.about-img-wrap-d5\{position:relative;\}', '.about-img-wrap-d5{position:relative;order:2;}', css)

# Make sure .about-d5 grid works with order (by default grid items respect order)
# Actually, wait, let's just use flex or order
if '.about-text-d5{order:1;}' not in css:
    css = re.sub(r'\.about-text-d5\{', '.about-text-d5{order:1;', css)
    css = re.sub(r'\.about-img-wrap-d5\{', '.about-img-wrap-d5{order:2;', css)

with open(css_path, 'w') as f:
    f.write(css)

print("Restored logo exactly from git")
