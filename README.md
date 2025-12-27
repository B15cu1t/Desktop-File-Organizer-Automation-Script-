# 📁 Desktop File Organizer (Automation Script)

## Overview
The **Desktop File Organizer** is a Python-based automation tool designed to keep a user's desktop clean, structured, and clutter-free. The script scans all files located on the desktop, identifies their file types, and automatically organizes them into predefined category folders.

This project was built to solve a real-world problem where desktops gradually become disorganized due to downloaded files, installers, media, and documents accumulating in a single location.

---

## Features
- Automatically scans the desktop directory
- Detects file types based on file extensions
- Creates category folders if they do not already exist
- Sorts files into organized directories:
  - 📷 Images
  - 🎵 Music
  - 🎬 Videos
  - 📄 Documents
  - 🧩 Applications / Installers
  - 🎮 Games
- Prevents overwriting existing files
- Fully local execution (no internet or external services required)

---

## How It Works
1. The script locates the user's desktop directory
2. Each file is analyzed based on its extension
3. A category is assigned according to predefined rules
4. If the destination folder does not exist, it is created automatically
5. Files are moved into their respective folders, resulting in a clean and organized desktop

---

## Technologies Used
- **Python**
- `os` — filesystem navigation and directory management
- `shutil` — secure file moving operations

---

## Why This Project Matters
This project demonstrates practical automation and scripting skills, including:
- File system manipulation
- Operating system interaction
- Problem-solving through automation
- Writing clean and reusable scripts

Unlike demonstration-only projects, this tool is designed for real-world daily use and can be easily extended with additional features.

---

## Potential Improvements
- Graphical user interface (GUI)
- User-defined categories and rules
- Scheduled automatic execution
- Logging and undo functionality
- Recursive folder organization

---

## Disclaimer
This script modifies local files by moving them into categorized folders. Users are encouraged to review the code and test it in a controlled environment before regular use.
