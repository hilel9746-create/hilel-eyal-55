import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# 1. Shrink the width of the right column to 45% (makes the image naturally smaller without grey bars)
# Find the hero-d5 grid columns
css = re.sub(r'grid-template-columns:1fr 1fr;', 'grid-template-columns:55% 45%;', css)

# 2. Shrink the height of the houses (from 25% to 18%) and give portrait 82%
css = re.sub(r'grid-template-rows:75% 25%;', 'grid-template-rows:82% 18%;', css)

# 3. Fine tune object-position to perfect center top crop
css = re.sub(r'object-position:center 12%;', 'object-position:center 8%;', css)

with open(file_path, 'w') as f:
    f.write(css)

print("Fine-tuned layout successfully")
