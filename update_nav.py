import re

html_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/index.html'

with open(html_path, 'r') as f:
    html = f.read()

new_nav = """<!-- ══ NAV ══ -->
<nav class="nav-d5">
  <div class="n-logo"><a href="index.html" style="text-decoration:none;color:inherit;">Cash<em>Buyers</em>Ohio</a></div>
  <div class="n-links">
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="contact.html">Contact</a>
    <a href="Calculator.html">Calculator</a>
  </div>
  <a href="appointment.html" class="n-cta">Get Cash Offer →</a>
</nav>

<!-- ══ HERO ══ -->"""

html = re.sub(r'<!-- ══ NAV ══ -->.*?<!-- ══ HERO ══ -->', new_nav, html, flags=re.DOTALL)

with open(html_path, 'w') as f:
    f.write(html)

css_to_append = """
/* ── DESIGN 5 NAV ── */
.nav-d5 {
  padding: 16px 60px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(255,255,255,.92);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border);
  font-family: var(--font-sans);
}
.n-logo { font-weight: 900; font-size: 1.25rem; letter-spacing: -0.5px; color: var(--navy); }
.n-logo em { color: var(--blue); font-style: normal; }
.n-links a {
  color: var(--gray); text-decoration: none; font-size: 0.95rem; font-weight: 500;
  margin-left: 28px; transition: color .2s;
}
.n-links a:hover { color: var(--navy); }
.n-cta {
  background: var(--blue) !important; color: #fff !important; padding: 12px 24px; border-radius: 8px;
  font-weight: 600; font-size: 0.9rem; text-decoration: none; transition: all .2s; display: inline-block;
}
.n-cta:hover { background: var(--blue-dk) !important; transform: translateY(-2px); box-shadow: 0 8px 20px rgba(37,99,235,.25); }

@media(max-width:860px){
  .nav-d5 { padding: 16px 20px; }
  .n-links { display: none; }
}
"""

css_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'
with open(css_path, 'a') as f:
    f.write(css_to_append)

print("Updated nav HTML and appended nav CSS")
