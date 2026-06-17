import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Make the gradient much more noticeable
css = css.replace('background: linear-gradient(135deg, #ffffff 0%, #f2f2ed 100%);', 'background: linear-gradient(135deg, #ffffff 0%, #e8e6df 100%);')

with open(file_path, 'w') as f:
    f.write(css)

print("Updated to a more visible gradient")
