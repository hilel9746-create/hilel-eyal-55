file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# The original line:
# .portrait-zone-d5 img{width:100%;height:100%;object-fit:cover;object-position:center top;}
old_line = '.portrait-zone-d5 img{width:100%;height:100%;object-fit:cover;object-position:center top;}'
new_line = '.portrait-zone-d5 img{width:100%;height:100%;object-fit:cover;object-position:center top;transform:scale(0.85) translateY(-8%);}'

css = css.replace(old_line, new_line)

with open(file_path, 'w') as f:
    f.write(css)

print("Updated image CSS successfully")
