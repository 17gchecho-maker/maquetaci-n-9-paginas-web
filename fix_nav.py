import os
import glob

directory = r"c:\Users\17gch\OneDrive\Escritorio\Checho\programación\diagramaMaquetación"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace(
        'data-bs-target="#navbarNavAltMarkup"', 
        'data-bs-target="#navbarNav"'
    )
    content = content.replace(
        'aria-controls="navbarNavAltMarkup"', 
        'aria-controls="navbarNav"'
    )
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Fixed {len(html_files)} files.")
