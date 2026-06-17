import glob
import os
import re

cwd = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website'
html_files = glob.glob(os.path.join(cwd, '*.html'))

hamburger_btn = """  <button class="hamburger" id="nav-toggle" aria-label="Toggle navigation">
    <span></span><span></span><span></span>
  </button>
</nav>"""

sticky_cta = """
<!-- Sticky Bottom CTA (Mobile Only) -->
<div class="mobile-bottom-cta-d5">
  <a href="appointment.html" class="n-cta-bottom">Get My Cash Offer</a>
</div>
</body>"""

new_script = """<script>
  const navToggle = document.getElementById('nav-toggle');
  const mobileMenu = document.getElementById('mobile-menu');
  if (navToggle && mobileMenu) {
    navToggle.addEventListener('click', function() {
      navToggle.classList.toggle('open');
      mobileMenu.classList.toggle('open');
    });
    // Close menu when clicking a link
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navToggle.classList.remove('open');
        mobileMenu.classList.remove('open');
      });
    });
  }

  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if(e.isIntersecting) e.target.classList.add('visible'); });
  }, {threshold: 0.1});
  document.querySelectorAll('.reveal,.reveal-left,.reveal-right').forEach(el => io.observe(el));
</script>"""

for file_path in html_files:
    file_name = os.path.basename(file_path)
    if file_name.lower() in ['calculator.html', 'old_index.html']:
        continue
    
    with open(file_path, 'r') as f:
        html = f.read()
    
    # Check if this file has the D5 nav
    if 'nav-d5' in html:
        # Add ID to n-links
        html = html.replace('<div class="n-links">', '<div class="n-links" id="mobile-menu">')
        
        # Insert hamburger button if not present
        if 'id="nav-toggle"' not in html:
            html = html.replace('</nav>', hamburger_btn, 1)
        
        # Insert sticky bottom CTA before body if not present
        if 'mobile-bottom-cta-d5' not in html:
            html = html.replace('</body>', sticky_cta, 1)
            
        # Replace old script logic
        # Some files might have different old script blocks, so let's safely replace the hamburger section
        # Or replace the whole script if it has IntersectionObserver
        if "const io =" in html and "document.getElementById('hamburger')" in html:
            # We can use regex to replace the whole <script>...</script> at the bottom
            # Actually, let's just replace the old hamburger logic block
            old_hamburger_logic = r"const hamburger = document\.getElementById\('hamburger'\);\s*if \(hamburger\) \{\s*hamburger\.addEventListener\('click', function\(\) \{\s*const navLinks = document\.getElementById\('nav-links'\);\s*if \(navLinks\) navLinks\.classList\.toggle\('active'\);\s*\}\);\s*\}"
            new_hamburger_logic = """const navToggle = document.getElementById('nav-toggle');
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
  }"""
            html = re.sub(old_hamburger_logic, new_hamburger_logic, html)
        
        with open(file_path, 'w') as f:
            f.write(html)
        print(f"Updated HTML in {file_name}")

print("HTML update complete.")
