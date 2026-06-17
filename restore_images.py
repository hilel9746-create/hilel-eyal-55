import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/index.html'

with open(file_path, 'r') as f:
    html = f.read()

# Image 1: Single Family
html = re.sub(r'https://images\.unsplash\.com/photo-1568605114967-8130f3a36994\?[^"]+', 'assets/images/condition-single-family.jpg', html)

# Image 2: Fixer Upper
html = re.sub(r'https://images\.unsplash\.com/photo-1570129477492-45c003edd2be\?[^"]+', 'assets/images/condition-fixer-upper.jpg', html)

# Image 3: Any Situation
html = re.sub(r'https://images\.unsplash\.com/photo-1449844908441-8829872d2607\?[^"]+', 'assets/images/condition-any-situation.jpg', html)

with open(file_path, 'w') as f:
    f.write(html)

print("Restored original local images")
