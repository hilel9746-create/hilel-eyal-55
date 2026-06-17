import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Nudge it down just a tiny bit
if 'min-height:calc(100vh - 155px);' in css:
    css = css.replace('min-height:calc(100vh - 155px);', 'min-height:calc(100vh - 148px);')

with open(file_path, 'w') as f:
    f.write(css)

print("Nudged divider down")
