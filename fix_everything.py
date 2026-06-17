import re

html_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/index.html'
css_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

# --- HTML FIXES ---
with open(html_path, 'r') as f:
    html = f.read()

# Change h1 to take less vertical space
html = html.replace('<h1>Sell Your Home.<br><em>Skip the</em><br>Hassle.</h1>', '<h1>Sell Your Home. <em>Skip the</em><br>Hassle.</h1>')

with open(html_path, 'w') as f:
    f.write(html)


# --- CSS FIXES ---
with open(css_path, 'r') as f:
    css = f.read()

# 1. Remove the grey padding around the portrait
css = re.sub(r'\.portrait-zone-d5\{position:relative;overflow:hidden; height:100%; padding: 0 12%;\}', 
             '.portrait-zone-d5{position:relative;overflow:hidden; height:100%;}', css)

# 2. Adjust grid template rows to give portrait more height (fixes the chin cut)
if '.hero-right-bg-d5{position:absolute;inset:0;display:grid;grid-template-rows:65% 35%;}' in css:
    css = css.replace('.hero-right-bg-d5{position:absolute;inset:0;display:grid;grid-template-rows:65% 35%;}',
                      '.hero-right-bg-d5{position:absolute;inset:0;display:grid;grid-template-rows:75% 25%;}')
else:
    # Use regex if spacing differs
    css = re.sub(r'\.hero-right-bg-d5\{[^\}]+\}', '.hero-right-bg-d5{position:absolute;inset:0;display:grid;grid-template-rows:75% 25%;}', css)

# 3. Ensure the image object-position is top to show face
css = re.sub(r'\.portrait-zone-d5 img\{width:100%;height:100%;object-fit:cover;object-position:[^\}]+;\}', 
             '.portrait-zone-d5 img{width:100%;height:100%;object-fit:cover;object-position:center top;}', css)

# 4. Make hero min-height instead of fixed height so it never cuts off content
css = re.sub(r'\.hero-d5\{height:calc\(100vh - 140px\);min-height:550px;padding-top:0;display:grid;grid-template-columns:1fr 1fr;overflow:hidden;background:#fafaf8;\}', 
             '.hero-d5{min-height:calc(100vh - 140px);padding-top:0;display:grid;grid-template-columns:1fr 1fr;overflow:hidden;background:#fafaf8;}', css)

# 5. Fix house strip so it fills the 25% height smoothly without looking squished (object-fit cover does this automatically but just to be sure)
css = re.sub(r'\.house-strip-d5 .hs-d5\{overflow:hidden;aspect-ratio:4/3;border-radius:4px; height: 100%;\}',
             '.house-strip-d5 .hs-d5{overflow:hidden;border-radius:4px; height: 100%;}', css)

with open(css_path, 'w') as f:
    f.write(css)

print("HTML and CSS fixes applied successfully")
