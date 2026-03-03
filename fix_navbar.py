import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The navbar toggler currently targets #navbarNavAltMarkup but the div ID is navbarNav
    new_content = content.replace('data-bs-target="#navbarNavAltMarkup"', 'data-bs-target="#navbarNav"')
    new_content = new_content.replace('aria-controls="navbarNavAltMarkup"', 'aria-controls="navbarNav"')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed navbar toggle in {filepath}')
