import re
import glob
import os

cwd = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website'
html_files = glob.glob(os.path.join(cwd, '*.html'))

new_nav = """<nav class="nav-d5">
  <div class="n-logo"><a href="index.html" style="text-decoration:none;color:inherit;">Cash<em>Buyers</em>Ohio</a></div>
  <div class="n-links">
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="contact.html">Contact</a>
    <a href="Calculator.html">Calculator</a>
  </div>
  <a href="appointment.html" class="n-cta">Get Cash Offer &rarr;</a>
</nav>"""

for file_path in html_files:
    file_name = os.path.basename(file_path)
    if file_name.lower() in ['index.html', 'calculator.html']:
        continue
    
    with open(file_path, 'r') as f:
        html = f.read()
    
    # Replace the old <nav>...</nav> block with the new nav
    # The old nav could have class, id etc. but usually it's <nav>
    # In index it was <nav class="nav-d5"> but we skip index.
    
    # Check if there is a <nav tag
    if '<nav' in html:
        new_html = re.sub(r'<nav[^>]*>.*?</nav>', new_nav, html, flags=re.DOTALL)
        
        # Check if the replacement was successful
        if new_html != html:
            with open(file_path, 'w') as f:
                f.write(new_html)
            print(f"Updated nav in {file_name}")

print("Navigation update complete.")
