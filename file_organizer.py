import os, shutil
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.csv'],
    'Videos': ['.mp4', '.mov', '.mkv', '.avi', '.flv', '.wmv', '.webm'],
    'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'PPTs': ['.ppt', '.pptx', '.key'],
    'Code': ['.py', '.cpp', '.c', '.java', '.js', '.html', '.css', '.php', '.json', '.xml'],
    'Executables': ['.exe', '.msi', '.bat', '.sh'],
    'Designs': ['.psd', '.ai', '.xd', '.fig', '.sketch'],
    'Others': []  # fallback category
}
folder_path = input("Enter folder path: ")

for file in os.listdir(folder_path):
    name, ext = os.path.splitext(file)
    for category, extensions in file_types.items():
        if ext.lower() in extensions:
            dest_folder = os.path.join(folder_path, category)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(os.path.join(folder_path, file), os.path.join(dest_folder, file))
            break
print("✅ Files organized successfully!")
# This script organizes files in a specified folder into subfolders based on their file types.
