import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Make the hero min-height dynamic to fit the viewport exactly
css = css.replace('min-height:75vh;', 'min-height:calc(100vh - 145px);')

with open(file_path, 'w') as f:
    f.write(css)

print("Updated min-height for responsive design")
