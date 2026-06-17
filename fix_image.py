import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Remove transform and set object-position to crop top
old_img = '.portrait-zone-d5 img{width:100%;height:100%;object-fit:cover;object-position:center top;transform:scale(0.85) translateY(-8%);}'
new_img = '.portrait-zone-d5 img{width:100%;height:100%;object-fit:cover;object-position:center 15%;}'

css = css.replace(old_img, new_img)

# Make the hero section shorter so the image isn't so huge
css = css.replace('min-height:90vh;', 'min-height:75vh;')

with open(file_path, 'w') as f:
    f.write(css)

print("Fixed image crop and layout gaps")
