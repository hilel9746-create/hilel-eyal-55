import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

html_files = [
    'index.html',
    'home.html',
    'about.html',
    'contact.html',
    'appointment.html',
    'privacy-policy.html',
    'terms-and-conditions.html'
]

# We want to find the logo img tag and replace its src, and add clear inline styles.
# It usually has alt="Logo" or src containing "logo" or "hillel"
img_pattern = re.compile(r'(<img\s+[^>]*?)src="([^"]*)"([^>]*>)', re.IGNORECASE)

for file in html_files:
    file_path = ROOT / file

    if not file_path.exists():
        print(f"Skipping {file}, does not exist.")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def img_repl(match):
        pre_src = match.group(1)
        src = match.group(2)
        post_src = match.group(3)

        # Check if it's a logo
        is_logo = False
        if 'alt="Logo"' in match.group(0):
            is_logo = True
        elif 'logo' in src.lower() or 'hillel' in src.lower():
            if (
                'hillel_logo_clean.png' in src.lower()
                or 'hillel_home_logo.png' in src.lower()
                or 'logo_new' in src.lower()
                or 'logo_header' in src.lower()
                or 'logo_transparent' in src.lower()
            ):
                is_logo = True
        
        if is_logo:
            new_src = 'assets/images/hillel_home_logo.png?v=home-yellow-2'
            # Remove any existing background or background-color from style
            style_pattern = re.compile(r'style="([^"]*)"')
            style_match = style_pattern.search(match.group(0))
            if style_match:
                style_content = style_match.group(1)
                # Remove background stuff
                style_content = re.sub(r'background(-color)?\s*:\s*[^;]+;?', '', style_content)
                style_content = re.sub(r'box-shadow\s*:\s*[^;]+;?', '', style_content)
                style_content = re.sub(r'filter\s*:\s*[^;]+;?', '', style_content)
                
                # add our clean styles
                new_style = f'style="{style_content.strip()} background: transparent !important; background-color: transparent !important; box-shadow: none !important; filter: none !important;"'
                
                # replace old style with new style in the whole tag parts
                pre_src_new = style_pattern.sub(new_style, pre_src)
                post_src_new = style_pattern.sub('', post_src) if new_style in pre_src_new else style_pattern.sub(new_style, post_src)
                
                # if style was in post_src, but we already replaced it in pre_src?
                # Actually, simple way:
                pass
            
            # simpler approach: just reconstruct the tag safely
            # first, remove old style="..." entirely
            tag_without_style = re.sub(r'style="[^"]*"', '', match.group(0))
            # replace src
            tag_new_src = re.sub(r'src="[^"]*"', f'src="{new_src}"', tag_without_style)
            # add our style at the end before >
            new_style = 'style="width:140px !important; max-height:45px !important; object-fit:contain !important; background:transparent !important; background-color:transparent !important; box-shadow:none !important; border:none !important; filter:none !important;"'
            
            final_tag = tag_new_src[:-1].strip() + ' ' + new_style + '>'
            return final_tag

        return match.group(0)

    new_content = img_pattern.sub(img_repl, content)
    
    # Also we want to ensure .image-container has no background if it wraps a logo
    # Instead of complex regex, we can just remove background:#000 from the whole file or similar inline styles
    new_content = re.sub(r'background:\s*(#000|#000000|black)\b', 'background: transparent', new_content, flags=re.IGNORECASE)
    new_content = re.sub(r'background-color:\s*(#000|#000000|black)\b', 'background-color: transparent', new_content, flags=re.IGNORECASE)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"No changes for {file}")
