import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Completely clean up the order styles
css = re.sub(r'order:\s*-?\d+;', '', css)

# Now we want the image on the LEFT. The HTML order is already image first, then text!
# So by removing all 'order' styles, the image naturally returns to the left.
# Just to be 100% sure, let's explicitly set the image to order -1 and text to order 1
if '.about-img-wrap-d5' in css:
    css = css.replace('.about-img-wrap-d5{', '.about-img-wrap-d5{order:-1;')

if '.about-text-d5{' in css:
    css = css.replace('.about-text-d5{', '.about-text-d5{order:1;')
else:
    # If the class doesn't exist, append it
    css += '\n.about-text-d5{order:1;}'

with open(file_path, 'w') as f:
    f.write(css)

print("Fixed the order properly!")
