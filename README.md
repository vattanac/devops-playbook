# DevOps Playbook

A documentation browser with a VS Code-style dark sidebar that mirrors your project folder structure.

## Quick Start

1. **Generate the folder structure:**

   ```bash
   python3 build_menu.py
   ```

2. **Serve the project locally** (required for the sidebar to load):

   ```bash
   python3 -m http.server 8000
   ```

3. **Open in your browser:**

   ```
   http://localhost:8000
   ```

## How It Works

The project uses two key files:

- **`build_menu.py`** — Scans the project directory and outputs `folder_structure.json`, a tree of all folders and files.
- **`index.html`** — The main page. It reads `folder_structure.json` and renders a collapsible sidebar navigation. Clicking a file loads it in the right-hand content panel.

Files like `.html`, `.pdf`, images, and text files preview directly in the browser. Non-previewable files (e.g. `.docx`) show a download button instead.

## Adding New Content

To add a new certification or topic:

1. Create a subfolder (e.g. `CKA/Scheduling/`).
2. Add your `index.html` and/or `document.docx` files inside it.
3. Re-run the build script:

   ```bash
   python3 build_menu.py
   ```

4. Refresh the browser — the sidebar updates automatically.

### Example folder structure

```
devops-playbook/
├── KCNA/
│   └── kubernetes-services/
│       ├── index.html
│       └── document.docx
├── CKA/
│   ├── Core Concepts/
│   │   ├── index.html
│   │   └── document.docx
│   └── Scheduling/
│       ├── index.html
│       └── document.docx
├── build_menu.py
├── folder_structure.json
├── index.html
└── README.md
```

## Features

- **Collapsible folder tree** — click folders to expand/collapse
- **File search** — filter files instantly with the search box
- **In-browser preview** — HTML, PDF, images, and text files load in the content panel
- **Download prompt** — non-previewable files offer a download button
- **Resizable sidebar** — drag the sidebar edge to adjust width
- **Auto-scan** — `build_menu.py` picks up any new files or folders automatically

## Customization

In `build_menu.py` you can:

- Edit the `EXCLUDED` set to hide specific files or folders from the tree.
- Set `INCLUDE_EXTENSIONS` to filter by file type (e.g. `{'.html', '.docx'}`).

