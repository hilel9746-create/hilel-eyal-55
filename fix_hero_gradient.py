import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Replace the solid #fafaf8 beige with the new visible beige gradient globally
css = css.replace('background:#fafaf8;', 'background: linear-gradient(135deg, #ffffff 0%, #e8e6df 100%);')
# Also catch cases with spaces
css = css.replace('background: #fafaf8;', 'background: linear-gradient(135deg, #ffffff 0%, #e8e6df 100%);')

with open(file_path, 'w') as f:
    f.write(css)

print("Applied gradient to hero and other sections")
