import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

new_gradient = 'linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)'
new_gradient_important = 'linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important'

# 1. Fix the divider strip to be slightly less dramatic
css = css.replace('background:linear-gradient(135deg, #3b82f6 0%, #1e3a8a 100%)', f'background:{new_gradient}')

# 2. Update all blue buttons
def update_bg(selector, css_text, new_bg):
    # Find the selector block
    pos = css_text.find(selector)
    if pos == -1:
        return css_text
    start_brace = css_text.find('{', pos)
    end_brace = css_text.find('}', start_brace)
    block = css_text[start_brace:end_brace]
    
    # Replace background inside block
    # Could be background:var(--blue); or background: var(--blue) !important;
    new_block = re.sub(r'background:\s*var\(--blue\)\s*!important', f'background: {new_gradient_important}', block)
    new_block = re.sub(r'background:\s*var\(--blue\)', f'background: {new_gradient}', new_block)
    
    return css_text[:start_brace] + new_block + css_text[end_brace:]

css = update_bg('.btn-blue', css, new_gradient)
css = update_bg('.btn-cobalt', css, new_gradient)
css = update_bg('.btn-main-d5', css, new_gradient)
css = update_bg('.cta-action-d5 a', css, new_gradient)
css = update_bg('.n-cta', css, new_gradient)
css = update_bg('.mobile-bottom-cta-d5 .n-cta-bottom', css, new_gradient)

# There is also a global button that might be affected:
css = update_bg('.btn, .btn-primary', css, new_gradient) # if exists

with open(file_path, 'w') as f:
    f.write(css)

print("Updated blue buttons to use gradient")
