import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Restore balance
if 'min-height:calc(100vh - 200px);' in css:
    css = css.replace('min-height:calc(100vh - 200px);', 'min-height:calc(100vh - 155px);')

with open(file_path, 'w') as f:
    f.write(css)

print("Restored divider height")
