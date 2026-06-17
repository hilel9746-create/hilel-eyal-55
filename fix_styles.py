import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# Replace colors in the D5 section
# #2e7d32 -> var(--blue)
# #1b5e20 -> var(--blue-dk)
# #e8f5e9 -> var(--blue-lt)

# But only in the classes that end with -d5 to be safe
# Since I appended it at the end under /* ── DESIGN 5 SECTIONS (HOMEPAGE) ── */, I can split and process only that part.
parts = css.split('/* ── DESIGN 5 SECTIONS (HOMEPAGE) ── */')

if len(parts) == 2:
    original_css = parts[0]
    d5_css = parts[1]
    
    # Colors
    d5_css = d5_css.replace('#2e7d32', 'var(--blue)')
    d5_css = d5_css.replace('#1b5e20', 'var(--blue-dk)')
    d5_css = d5_css.replace('#e8f5e9', 'var(--blue-lt)')
    
    # Spacing
    d5_css = d5_css.replace('padding-top:40px;', 'padding-top:0;')
    d5_css = d5_css.replace('padding:80px 60px;', 'padding:20px 60px 80px 60px;')
    d5_css = d5_css.replace('padding:60px 24px;', 'padding:20px 24px 60px 24px;') # for mobile hero-left-d5
    
    new_css = original_css + '/* ── DESIGN 5 SECTIONS (HOMEPAGE) ── */' + d5_css
    
    with open(file_path, 'w') as f:
        f.write(new_css)
    print("Updated colors and spacing successfully.")
else:
    print("Could not find the D5 section marker.")
