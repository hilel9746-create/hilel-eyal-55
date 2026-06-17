import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Add gap: 10px !important; to .about-d5 in the mobile query
# The mobile query we added earlier has:
# .about-d5{grid-template-columns:1fr !important; padding:60px 24px !important;}
css = css.replace(
    '.about-d5{grid-template-columns:1fr !important; padding:60px 24px !important;}',
    '.about-d5{grid-template-columns:1fr !important; padding:60px 24px !important; gap: 10px !important;}'
)

# Also reduce padding on the logo frame on mobile to bring it even tighter
if '.about-img-frame-d5{' not in css.split('@media(max-width:860px)')[1]:
    # It's not in the mobile block yet, let's inject it into the mobile block
    # Actually, we can just append it right before the closing brace of the mobile block
    
    # We know my pristine mobile block has this line:
    # .trust-row-d5{justify-content:center !important;}
    css = css.replace(
        '.trust-row-d5{justify-content:center !important;}',
        '.trust-row-d5{justify-content:center !important;}\n  .about-img-frame-d5{padding: 10px !important;}'
    )

with open(file_path, 'w') as f:
    f.write(css)

print("Reduced gap on mobile")
