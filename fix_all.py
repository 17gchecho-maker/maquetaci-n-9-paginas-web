import os, glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix index1.html reference to index.html
    new_content = content.replace('href="index1.html"', 'href="index.html"')
    
    # 2. Fix viewport just in case (most already have it, but let's check)
    if 'name="viewport"' not in new_content:
        new_content = new_content.replace('<head>', '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1">')
        
    # 3. Fix Bootstrap layout typos (col-lm- to col-lg-, xol-xxl- to col-xxl-)
    new_content = new_content.replace('col-lm-', 'col-lg-')
    new_content = new_content.replace('xol-xxl-', 'col-xxl-')
    
    # 4. Fix specific CSS links if broken
    # index.html uses style.css (was style1.css but seems already style.css from grep). Let's enforce it.
    if filepath == 'index.html':
        new_content = new_content.replace('href="style1.css"', 'href="style.css"')
        new_content = new_content.replace('href="index1.css"', 'href="style.css"')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed {filepath}')
