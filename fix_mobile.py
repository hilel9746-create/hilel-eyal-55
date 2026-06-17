import re

file_path = '/Users/itaykarkason/Python Projects/hillel/cashbuyersohio_website/assets/css/style.css'

with open(file_path, 'r') as f:
    css = f.read()

# We need to replace everything inside the first @media(max-width:860px) that applies to D5
# To be safe, let's locate the D5 section entirely.
# Let's just append the correct mobile styles at the very end of the file using !important where needed,
# or cleanly replace the block.
# Actually, let's just find the exact block and replace it.

start_marker = '@media(max-width:860px){'
blocks = css.split(start_marker)

# The D5 mobile block is likely the second one, or the one containing .hero-d5.
new_css = blocks[0]

for i in range(1, len(blocks)):
    block = blocks[i]
    if '.hero-d5' in block and '.about-d5' in block:
        # This is the corrupted D5 mobile block!
        # Let's replace it with the correct rules.
        # Find the end of this block (the first unmatched '}')
        
        # simple way: just rewrite the D5 mobile rules and let CSS cascade handle it by appending at the very bottom
        pass
        
    new_css += start_marker + block

# Now let's forcefully append the pristine mobile rules at the very end of the file.
pristine_mobile = """
@media(max-width:860px){
  .hero-d5{grid-template-columns:1fr !important; height:auto !important; min-height:auto !important; overflow:visible !important; display: flex !important; flex-direction: column !important;}
  .hero-left-d5{padding:40px 24px !important; display:flex; flex-direction:column; justify-content:center;}
  .hero-right-d5{min-height:550px !important; position:relative !important; width:100% !important;}
  .hero-right-bg-d5{position:absolute;inset:0;display:grid;grid-template-rows:70% 30% !important;}
  .hero-left-d5 h1{font-size:2.2rem !important; margin-bottom:12px !important;}
  .about-d5{grid-template-columns:1fr !important; padding:60px 24px !important;}
  .prop-grid-d5{grid-template-columns:1fr !important;}
  .cta-d5{grid-template-columns:1fr !important; gap:24px !important; padding: 40px 24px !important;}
  .divider-strip-d5{gap:28px !important; padding:18px 24px !important; justify-content:center !important;}
  .trust-row-d5{justify-content:center !important;}
}
"""

with open(file_path, 'w') as f:
    f.write(new_css + pristine_mobile)

print("Fixed mobile layout")
