import os
import re

directory = '.'

mapping = [
    ("Harold & Angela", "index.html"),
    ("Kevin & Nicoll", "index2.html"),
    ("Sara & Dahiana", "index3.html"),
    ("Alejandra & Daniel", "index4.html"),
    ("Mariana & Nicoll", "index5.html"),
    ("Ivan & Eduardo", "index6.html"),
    ("Duvan & Yojan", "index7.html"),
    ("Sofia & Gabriela", "index8.html"),
    ("Stefania & Andrea", "index9.html"),
]

html_files = [f"index{i}.html" for i in range(1, 10)]

for filename in html_files:
    if not os.path.exists(filename) and filename == "index1.html":
        # Maybe already renamed
        continue
    
    filepath = os.path.join(directory, filename)
    if not os.path.exists(filepath):
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace index1.html with index.html
    content = content.replace('href="index1.html"', 'href="index.html"')
    
    # 2. Fix the active class in navbar
    # First, remove active and aria-current="page" from all nav-links
    content = re.sub(r'class="nav-link active"', 'class="nav-link"', content)
    content = re.sub(r'aria-current="page"\s*', '', content)
    
    # Now, find the link for the current file and add active class and aria-current
    target_filename = "index.html" if filename == "index1.html" else filename
    
    # We want to replace `<a class="nav-link" href="target_filename">`
    # with `<a class="nav-link active" aria-current="page" href="target_filename">`
    pattern = r'(<a class="nav-link")\s*(href="' + re.escape(target_filename) + r'")'
    replacement = r'\1 active" aria-current="page" \2'
    content = re.sub(pattern, replacement, content)

    # Note: If target_filename didn't replace because there was extra spacing, let's use a more flexible regex:
    pattern2 = r'(class="nav-link"\s+href="' + re.escape(target_filename) + r'")'
    replacement2 = r'class="nav-link active" aria-current="page" href="' + target_filename + '"'
    content = re.sub(pattern2, replacement2, content)

    # Some might be <a class="nav-link " href="...">
    pattern3 = r'(class="nav-link\s+"\s+href="' + re.escape(target_filename) + r'")'
    content = re.sub(pattern3, replacement2, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

if os.path.exists("index1.html"):
    os.rename("index1.html", "index.html")
    print("Renamed index1.html to index.html")
