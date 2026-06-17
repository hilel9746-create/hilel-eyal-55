import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Fix the house strip
css = css.replace('.house-strip-d5 .hs-d5{overflow:hidden;border-radius:50px; height: 100%;}', 
                  '.house-strip-d5 .hs-d5{overflow:hidden;border-radius:4px; height: 100%;}')

# Check for any form controls or other generic classes that had border-radius: 8px; replaced
css = css.replace('.form-control{width:100%;padding:12px;border:1px solid var(--border);border-radius:50px;',
                  '.form-control{width:100%;padding:12px;border:1px solid var(--border);border-radius:8px;')

with open(file_path, 'w') as f:
    f.write(css)

print("Restored house strip and forms.")
