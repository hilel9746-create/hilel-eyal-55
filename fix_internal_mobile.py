import re
import glob
import os

cwd = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website'

# 1. Update style.css
css_path = os.path.join(cwd, 'assets/css/style.css')
with open(css_path, 'r') as f:
    css = f.read()

grid_css = "\n.internal-grid-d5 { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }\n"
if '.internal-grid-d5' not in css:
    css = css.replace('/* ── CONTENT BLOCK', grid_css + '/* ── CONTENT BLOCK')
    
    # Add to mobile query
    mobile_query_end = css.rfind('}')
    # Actually, let's just use string replace on the mobile block
    css = css.replace('.prop-grid-d5{grid-template-columns:1fr !important;}', 
                      '.prop-grid-d5{grid-template-columns:1fr !important;}\n  .internal-grid-d5{grid-template-columns:1fr !important;}')

with open(css_path, 'w') as f:
    f.write(css)

# 2. Update contact.html and appointment.html and fix scripts in all HTML
html_files = glob.glob(os.path.join(cwd, '*.html'))

new_script = """<script>
  const navToggle = document.getElementById('nav-toggle');
  const mobileMenu = document.getElementById('mobile-menu');
  if (navToggle && mobileMenu) {
    navToggle.addEventListener('click', function() {
      navToggle.classList.toggle('open');
      mobileMenu.classList.toggle('open');
    });
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navToggle.classList.remove('open');
        mobileMenu.classList.remove('open');
      });
    });
  }
</script>"""

old_script_pattern = r"<script>\s*document\.getElementById\('hamburger'\)\.addEventListener\('click', function\(\) \{\s*document\.getElementById\('nav-links'\)\.classList\.toggle\('active'\);\s*\}\);\s*</script>"

for file_path in html_files:
    file_name = os.path.basename(file_path)
    with open(file_path, 'r') as f:
        html = f.read()
        
    changed = False
    
    if "display: grid; grid-template-columns: 1fr 1fr; gap: 40px;" in html:
        html = html.replace('style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;"', 'class="internal-grid-d5"')
        html = html.replace('class="content-inner" class="internal-grid-d5"', 'class="content-inner internal-grid-d5"')
        changed = True
        
    if "display: grid; grid-template-columns: 1fr 1fr; gap: 32px;" in html:
        html = html.replace('style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px;"', 'class="internal-grid-d5"')
        changed = True
        
    if re.search(old_script_pattern, html):
        html = re.sub(old_script_pattern, new_script, html)
        changed = True
        
    if changed:
        with open(file_path, 'w') as f:
            f.write(html)
        print(f"Fixed {file_name}")

print("Fixed internal mobile grids and scripts.")
