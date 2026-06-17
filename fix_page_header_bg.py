import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Replace the blue gradient with the beige #fafaf8
css = css.replace('background: linear-gradient(135deg, #eef2ff 0%, #ecfeff 100%);', 'background: #fafaf8;')

with open(file_path, 'w') as f:
    f.write(css)

print("Updated page header background to beige")
