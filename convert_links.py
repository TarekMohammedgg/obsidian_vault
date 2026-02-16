import os
import re

vault_path = "./" 
# Regex to find ![[image.png]]
pattern = re.compile(r'\!\[\[(.*?\.(?:png|jpg|jpeg|webp|gif|svg))\]\]')

for root, dirs, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            
            # Calculate depth for the relative path
            # count how many separators are in the path relative to the root
            rel_dir = os.path.relpath(root, vault_path)
            if rel_dir == ".":
                depth = 0
            else:
                depth = len(rel_dir.split(os.sep))
            
            prefix = "../" * depth + "assets/"

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # No space between [] and ()
            new_content = pattern.sub(rf'![]({prefix}\1)', content)

            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed: {file} (Depth: {depth})")