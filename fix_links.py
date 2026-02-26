import os
import re

directory = '.'

mapping = [
    ("Harold &amp; Angela", "index1.html"),
    ("Harold & Angela", "index1.html"),
    ("Kevin &amp; Nicoll", "index2.html"),
    ("Kevin & Nicoll", "index2.html"),
    ("Sara &amp; Dahiana", "index3.html"),
    ("Sara & Dahiana", "index3.html"),
    ("Alejandra &amp; Daniel", "index4.html"),
    ("Alejandra & Daniel", "index4.html"),
    ("Mariana &amp; Nicoll", "index5.html"),
    ("Mariana & Nicoll", "index5.html"),
    ("Ivan &amp; Eduardo", "index6.html"),
    ("Ivan & Eduardo", "index6.html"),
    ("Duvan &amp; Yojan", "index7.html"),
    ("Duvan & Yojan", "index7.html"),
    ("Sofia &amp; Gabriela", "index8.html"),
    ("Sofia & Gabriela", "index8.html"),
    ("Stefania &amp; Andrea", "index9.html"),
    ("Stefania & Andrea", "index9.html"),
]

for filename in os.listdir(directory):
    if filename.endswith(".html") and filename.startswith("index"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content
        for name, correct_href in mapping:
            pattern = r'(<a\s+[^>]*?href=)"([^"]*)"([^>]*>)\s*' + re.escape(name) + r'\s*(</a>)'
            new_content = re.sub(pattern, r'\g<1>"' + correct_href + r'"\g<3>' + name + r'\4', new_content, flags=re.IGNORECASE)

        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed links in {filename}")
