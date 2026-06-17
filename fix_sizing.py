import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Make sure hero-d5 has height and min-height
css = re.sub(r'\.hero-d5\{[^\}]+\}', '.hero-d5{height:calc(100vh - 140px);min-height:550px;padding-top:0;display:grid;grid-template-columns:1fr 1fr;overflow:hidden;background:#fafaf8;}', css)

# Update padding in hero-left-d5
css = re.sub(r'\.hero-left-d5\{[^\}]+\}', '.hero-left-d5{padding:30px 50px;display:flex;flex-direction:column;justify-content:center;background:#fafaf8;}', css)

# Shrink h1
css = re.sub(r'\.hero-left-d5 h1\{[^\}]+\}', '.hero-left-d5 h1{font-size:clamp(1.8rem,3vw,3.2rem);font-weight:900;line-height:1.05;letter-spacing:-1.5px;margin-bottom:12px;color:var(--navy);animation:fadeLeft .5s .1s ease both;}', css)

# Shrink desc
css = re.sub(r'\.h-desc-d5\{[^\}]+\}', '.h-desc-d5{font-size:0.95rem;color:var(--gray);line-height:1.6;max-width:400px;margin-bottom:20px;animation:fadeLeft .5s .2s ease both;}', css)

# Shrink owner card
css = re.sub(r'\.owner-card-d5\{[^\}]+\}', '.owner-card-d5{display:flex;align-items:center;gap:12px;background:#fff;border:1px solid var(--border);border-radius:10px;padding:12px 18px;margin-bottom:20px;box-shadow:0 2px 16px rgba(0,0,0,0.05);animation:fadeLeft .5s .3s ease both;}', css)
css = re.sub(r'\.owner-thumb-d5\{[^\}]+\}', '.owner-thumb-d5{width:46px;height:46px;border-radius:50%;object-fit:cover;object-position:center top;border:2px solid var(--blue);}', css)

# Shrink buttons
css = re.sub(r'\.hero-btns-d5\{[^\}]+\}', '.hero-btns-d5{display:flex;gap:12px;margin-bottom:16px;animation:fadeLeft .5s .4s ease both;}', css)
css = re.sub(r'\.btn-main-d5\{[^\}]+\}', '.btn-main-d5{background:var(--blue);color:#fff;padding:12px 24px;border-radius:4px;font-weight:700;font-size:0.88rem;text-decoration:none;transition:all .2s;display:inline-block;}', css)
css = re.sub(r'\.btn-outline-d5\{[^\}]+\}', '.btn-outline-d5{border:1.5px solid #ccc;color:var(--navy);padding:11px 22px;border-radius:4px;font-weight:600;font-size:0.85rem;text-decoration:none;transition:all .2s;display:inline-block;}', css)

# Shrink trust row
css = re.sub(r'\.trust-row-d5\{[^\}]+\}', '.trust-row-d5{display:flex;gap:10px 18px;flex-wrap:wrap;animation:fadeLeft .5s .5s ease both;}', css)

with open(file_path, 'w') as f:
    f.write(css)

print("Updated sizes successfully")
