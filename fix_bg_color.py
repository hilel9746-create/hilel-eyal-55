import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Replace the right-side background color (#f0f0ec) with the left-side background color (#fafaf8)
css = css.replace('background:#f0f0ec;', 'background:#fafaf8;')

with open(file_path, 'w') as f:
    f.write(css)

print("Unified background colors")
