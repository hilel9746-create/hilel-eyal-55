import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# h1 margin
css = re.sub(r'(\.hero-left-d5 h1\{[^}]*margin-bottom:)8px;', r'\g<1>18px;', css)

# desc margin
css = re.sub(r'(\.h-desc-d5\{[^}]*margin-bottom:)12px;', r'\g<1>24px;', css)

# owner card margin
css = re.sub(r'(\.owner-card-d5\{[^}]*margin-bottom:)16px;', r'\g<1>28px;', css)

# btns margin
css = re.sub(r'(\.hero-btns-d5\{[^}]*margin-bottom:)12px;', r'\g<1>24px;', css)

with open(file_path, 'w') as f:
    f.write(css)

print("Restored margins to make it less squished")
