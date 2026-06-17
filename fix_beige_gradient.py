import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Replace the solid beige with a beige gradient
css = css.replace('background: #fafaf8;', 'background: linear-gradient(135deg, #ffffff 0%, #f2f2ed 100%);')

with open(file_path, 'w') as f:
    f.write(css)

print("Updated beige background to a subtle gradient")
