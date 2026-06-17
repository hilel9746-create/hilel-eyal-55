import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Change the flex/grid order so the image is on the left (order:1) and text on the right (order:2)
css = css.replace('.about-text-d5{order:1;', '.about-text-d5{order:2;')
css = css.replace('.about-img-wrap-d5{order:2;', '.about-img-wrap-d5{order:1;')

with open(file_path, 'w') as f:
    f.write(css)

print("Moved logo to the left")
