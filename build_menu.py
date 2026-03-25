#!/usr/bin/env python3
"""
Scans the project folder structure and generates a folder_structure.json
file that the index.html sidebar uses to build the navigation tree.

Run this script whenever you add/remove/rename files or folders:
    python3 build_menu.py
"""

import os
import json

# Directory where this script lives (project root)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Files/folders to exclude from the tree
EXCLUDED = {
    'build_menu.py',
    'folder_structure.json',
    'index.html',
    'netlify.toml',
    'runtime.txt',
    'README.md',
    '.git',
    '.DS_Store',
    '__pycache__',
    'node_modules',
}

# File extensions to include (set to None to include everything)
INCLUDE_EXTENSIONS = None  # e.g., {'.html', '.docx', '.pdf'}


def scan_directory(path, relative_base=""):
    """Recursively scan a directory and return a tree structure."""
    items = []

    try:
        entries = sorted(os.listdir(path), key=lambda x: (not os.path.isdir(os.path.join(path, x)), x.lower()))
    except PermissionError:
        return items

    for entry in entries:
        if entry in EXCLUDED or entry.startswith('.'):
            continue

        full_path = os.path.join(path, entry)
        rel_path = os.path.join(relative_base, entry) if relative_base else entry

        if os.path.isdir(full_path):
            children = scan_directory(full_path, rel_path)
            if children:  # Only include folders that have content
                items.append({
                    "name": entry,
                    "type": "folder",
                    "path": rel_path,
                    "children": children
                })
        else:
            if INCLUDE_EXTENSIONS is None or os.path.splitext(entry)[1].lower() in INCLUDE_EXTENSIONS:
                items.append({
                    "name": entry,
                    "type": "file",
                    "path": rel_path
                })

    return items


def main():
    tree = scan_directory(BASE_DIR)
    output_path = os.path.join(BASE_DIR, "folder_structure.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(tree, f, indent=2, ensure_ascii=False)

    print(f"✅ folder_structure.json generated with {count_items(tree)} items")


def count_items(tree):
    count = 0
    for item in tree:
        count += 1
        if item["type"] == "folder":
            count += count_items(item["children"])
    return count


if __name__ == "__main__":
    main()
