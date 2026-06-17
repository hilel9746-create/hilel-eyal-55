import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Update .hero-d5 to have a strict height on desktop
css = css.replace('min-height:calc(100vh - 145px);', 'height:calc(100vh - 140px);min-height:600px;')

# Update padding in hero-left
css = css.replace('padding:20px 60px 80px 60px;', 'padding:0 60px;')
css = css.replace('padding:80px 60px;', 'padding:0 60px;')

# Reduce margins to save vertical space
css = css.replace('margin-bottom:32px;animation:fadeLeft .5s .2s ease both;', 'margin-bottom:20px;animation:fadeLeft .5s .2s ease both;') # desc
css = css.replace('margin-bottom:32px;box-shadow:', 'margin-bottom:20px;box-shadow:') # owner card
css = css.replace('margin-bottom:28px;animation:fadeLeft .5s .4s ease both;', 'margin-bottom:20px;animation:fadeLeft .5s .4s ease both;') # hero btns

# Make sure on mobile it goes back to auto height
css = css.replace('@media(max-width:860px){\n  .hero-d5{grid-template-columns:1fr;}', '@media(max-width:860px){\n  .hero-d5{grid-template-columns:1fr; height:auto; min-height:auto;}')

with open(file_path, 'w') as f:
    f.write(css)

print("Updated hero height and margins")
