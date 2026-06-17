import os
import glob

cwd = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website'
html_files = glob.glob(os.path.join(cwd, '*.html'))

for file_path in html_files:
    file_name = os.path.basename(file_path)
    if file_name.lower() == 'calculator.html':
        continue
    
    with open(file_path, 'r') as f:
        html = f.read()
    
    # Remove the calculator link
    if '<a href="Calculator.html">Calculator</a>' in html:
        new_html = html.replace('    <a href="Calculator.html">Calculator</a>\n', '')
        # Fallback if whitespace differs
        new_html = new_html.replace('<a href="Calculator.html">Calculator</a>', '')
        
        with open(file_path, 'w') as f:
            f.write(new_html)
        print(f"Removed calculator from {file_name}")

print("Done removing Calculator link.")
