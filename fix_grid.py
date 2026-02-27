import glob
import re

html_files = glob.glob('*.html')

def upgrade_grid(match):
    col_num = int(match.group(1))
    
    # Don't touch col-12 as it is already full width
    if col_num == 12:
        return 'col-12'
        
    # We want Mobile: col-12, Tablet: col-md-6 (or similar), PC: col-lg-{col_num}
    # For tablet, let's use a sensible default based on PC size
    tablet_num = 6
    if col_num > 6:
        tablet_num = 12
    elif col_num == 4 or col_num == 3:
        tablet_num = 6  # 2 per row
    elif col_num == 5 or col_num == 7:
        tablet_num = 12 
        
    return f'col-12 col-md-{tablet_num} col-lg-{col_num}'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all class="..."
    def replace_classes(class_match):
        class_str = class_match.group(1)
        
        # Check if it already has responsive classes
        if 'col-md-' in class_str or 'col-lg-' in class_str or 'col-sm-' in class_str:
            return f'class="{class_str}"'
            
        # Upgrade any col-\d+ inside
        # \bcol-(\d+)\b will match 'col-3', 'col-6', etc.
        new_class_str = re.sub(r'\bcol-(\d+)\b', upgrade_grid, class_str)
        
        if new_class_str != class_str:
            # Clean up potential duplicates just in case
            parts = new_class_str.split()
            seen = set()
            cleaned = []
            for p in parts:
                if p not in seen:
                    cleaned.append(p)
                    seen.add(p)
            new_class_str = ' '.join(cleaned)
            
        return f'class="{new_class_str}"'

    new_content = re.sub(r'class="([^"]*)"', replace_classes, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Upgraded grids in {filepath}')
