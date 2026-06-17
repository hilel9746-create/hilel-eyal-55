file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/index.html'

with open(file_path, 'r') as f:
    html = f.read()

# Fix the script by adding a null check for hamburger
old_script = """  document.getElementById('hamburger').addEventListener('click', function() {
    document.getElementById('nav-links').classList.toggle('active');
  });"""

new_script = """  const hamburger = document.getElementById('hamburger');
  if (hamburger) {
    hamburger.addEventListener('click', function() {
      const navLinks = document.getElementById('nav-links');
      if (navLinks) navLinks.classList.toggle('active');
    });
  }"""

html = html.replace(old_script, new_script)

with open(file_path, 'w') as f:
    f.write(html)

print("Fixed javascript error")
