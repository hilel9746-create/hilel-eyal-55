import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Change object-position to move the image up (crop from top) to show the chin
css = re.sub(r'\.portrait-zone-d5 img\{width:100%;height:100%;object-fit:cover;object-position:[^;]+;\}', 
             '.portrait-zone-d5 img{width:100%;height:100%;object-fit:cover;object-position:center 25%;}', css)

with open(file_path, 'w') as f:
    f.write(css)

print("Adjusted object position to show face")
