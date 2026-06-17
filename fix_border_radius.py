import re
file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'
with open(file_path, 'r') as f:
    css = f.read()

# Make the bottom mobile CTA pill-shaped (50px) or highly rounded (12px) to look more rounded.
# If the "Get Cash Offer ->" is 8px, maybe they just want the bottom one to be 50px so the sides are fully rounded.
css = css.replace('border-radius: 8px;', 'border-radius: 50px;')
css = css.replace('border-radius:4px;', 'border-radius:50px;')

with open(file_path, 'w') as f:
    f.write(css)
