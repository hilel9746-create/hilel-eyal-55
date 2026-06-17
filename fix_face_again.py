import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Change object-position from 25% to 12% to balance the crop
css = re.sub(r'object-position:center 25%;', 'object-position:center 12%;', css)

with open(file_path, 'w') as f:
    f.write(css)

print("Adjusted face crop")
