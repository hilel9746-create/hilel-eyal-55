import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Left column padding
css = re.sub(r'\.hero-left-d5\{padding:[^;]+;', '.hero-left-d5{padding:10px 50px;', css)

# Shrink h1 more
css = re.sub(r'\.hero-left-d5 h1\{font-size:[^;]+;font-weight:900;line-height:[^;]+;letter-spacing:-1\.5px;margin-bottom:12px;', 
             '.hero-left-d5 h1{font-size:clamp(1.6rem,2.8vw,2.8rem);font-weight:900;line-height:1.05;letter-spacing:-1px;margin-bottom:8px;', css)

# Shrink desc more
css = re.sub(r'\.h-desc-d5\{font-size:[^;]+;color:var\(--gray\);line-height:[^;]+;max-width:400px;margin-bottom:20px;', 
             '.h-desc-d5{font-size:0.88rem;color:var(--gray);line-height:1.5;max-width:400px;margin-bottom:12px;', css)

# Shrink owner card more
css = re.sub(r'\.owner-card-d5\{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid var\(--border\);border-radius:10px;padding:[^;]+;margin-bottom:20px;', 
             '.owner-card-d5{display:flex;align-items:center;gap:10px;background:#fff;border:1px solid var(--border);border-radius:10px;padding:8px 12px;margin-bottom:16px;', css)
css = re.sub(r'\.owner-thumb-d5\{width:[^;]+;height:[^;]+;', 
             '.owner-thumb-d5{width:40px;height:40px;', css)

# Shrink buttons more
css = re.sub(r'\.hero-btns-d5\{display:flex;gap:12px;margin-bottom:16px;', 
             '.hero-btns-d5{display:flex;gap:12px;margin-bottom:12px;', css)

# Fix image: add padding so it's narrower, which scales down the height automatically in object-fit cover
# Previous: .portrait-zone-d5{position:relative;overflow:hidden; height:100%;}
# Change to: .portrait-zone-d5{position:relative;overflow:hidden; height:100%; padding: 0 12%;}
css = re.sub(r'\.portrait-zone-d5\{position:relative;overflow:hidden; height:100%;\}', 
             '.portrait-zone-d5{position:relative;overflow:hidden; height:100%; padding: 0 12%;}', css)

# Change object-position to center 5% so it's slightly cut at the top but shows more face/chin
# Previous: .portrait-zone-d5 img{width:100%;height:100%;object-fit:cover;object-position:center 15%;}
css = re.sub(r'\.portrait-zone-d5 img\{width:100%;height:100%;object-fit:cover;object-position:[^\}]+;\}', 
             '.portrait-zone-d5 img{width:100%;height:100%;object-fit:cover;object-position:center 5%;}', css)

with open(file_path, 'w') as f:
    f.write(css)

print("Updated sizes successfully")
