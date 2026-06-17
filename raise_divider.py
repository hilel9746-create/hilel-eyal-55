import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Change calc(100vh - 140px) to calc(100vh - 200px) to pull the blue bar up more
if 'min-height:calc(100vh - 140px);' in css:
    css = css.replace('min-height:calc(100vh - 140px);', 'min-height:calc(100vh - 200px);')

with open(file_path, 'w') as f:
    f.write(css)

print("Raised divider strip successfully")
