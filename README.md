# 🗂️ File Organizer Script (Python)

Automatically organize your messy folders with a single Python script!  
This tool scans a directory and moves files into categorized subfolders based on their file extensions (Images, Documents, Code, etc.).

---

## 🚀 Features

- 🧠 Automatically detects and sorts files into categories  
- 📁 Creates folders for each file type if not already present  
- 🔁 Works on **Windows**, **macOS**, and **Linux**  
- ⚙️ Easily customizable (add your own categories and extensions)  
- ✅ Simple and lightweight — no external dependencies  

---

## 🧩 Categories Covered

| Category     | File Types |
|---------------|------------|
| **Images** | .jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg, .webp |
| **Documents** | .pdf, .doc, .docx, .txt, .rtf, .odt, .xls, .xlsx, .csv |
| **Videos** | .mp4, .mov, .mkv, .avi, .flv, .wmv, .webm |
| **Music** | .mp3, .wav, .flac, .aac, .ogg, .m4a |
| **Archives** | .zip, .rar, .7z, .tar, .gz |
| **PPTs** | .ppt, .pptx, .key |
| **Code Files** | .py, .cpp, .c, .java, .js, .html, .css, .php, .json, .xml |
| **Executables** | .exe, .msi, .bat, .sh |
| **Designs** | .psd, .ai, .xd, .fig, .sketch |
| **Others** | Any file not matching the above types |

---

## 🧰 Requirements

- Python **3.7+**
- No external libraries required (`os` and `shutil` are built-in)

---

## ✅ The script will:

- Scan your selected folder

- Create subfolders (Images, Documents, etc.)

- Move each file into its matching category

---
## 🧩 Customization

Want to add your own file type category?
Just edit this dictionary in file_organizer.py:

file_types = {
   - 'Images': ['.jpg', '.jpeg', '.png'],
   - 'MyCategory': ['.xyz', '.abc'],  # Add your custom types here
}

---

