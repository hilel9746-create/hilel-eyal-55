import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Hide the blue accent dots since it's a logo now, not a photo
css = re.sub(r'\.about-accent-d5\{position:absolute;[^}]+\}', '.about-accent-d5{display:none;}', css)

# Make the logo small and styled like it was in git (.services-img)
css = re.sub(r'\.about-img-frame-d5 img\{[^\}]+\}', '.about-img-frame-d5 img{width:100%;max-width:240px;height:auto;object-fit:contain;object-position:center;opacity:0.85;margin:0 auto;display:block;}', css)

# Adjust the frame to center the logo vertically
css = re.sub(r'\.about-img-frame-d5\{[^\}]+\}', '.about-img-frame-d5{display:flex;align-items:center;justify-content:center;padding:40px;}', css)

with open(file_path, 'w') as f:
    f.write(css)

print("Styled the logo based on git reference")
