import re

html_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/index.html'
css_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(html_path, 'r') as f:
    html = f.read()

# Replace the owner image in the About section with the home logo
html = html.replace(
    '<img src="https://cashbuyersohio.net/assets/images/hero-owner-professional.png" alt="Hilel — Founder"/>',
    '<img src="assets/images/hillel_home_logo.png" alt="Hillel\'s Team Logo"/>'
)

with open(html_path, 'w') as f:
    f.write(html)

with open(css_path, 'r') as f:
    css = f.read()

# Make sure the logo isn't cropped by object-fit: cover
# The original CSS was:
# .about-img-frame-d5 img{width:100%;height:100%;object-fit:cover;object-position:center top;}
css = re.sub(r'\.about-img-frame-d5 img\{[^\}]+\}', '.about-img-frame-d5 img{width:100%;height:100%;object-fit:contain;object-position:center;}', css)
css = re.sub(r'\.about-img-frame-d5\{[^\}]+\}', '.about-img-frame-d5{border-radius:12px;overflow:hidden;position:relative;background:transparent;padding:20px;}', css)

with open(css_path, 'w') as f:
    f.write(css)

print("Restored logo in About section")
