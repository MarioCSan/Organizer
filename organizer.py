import os
import shutil
from pathlib import Path

# Detecta automáticamente la carpeta Downloads
downloads = Path.home() / "Downloads"

folders = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Code": [".py", ".js", ".cs", ".java", ".html", ".css"],
    "Libros": [".epub", ".mobi", ".pdf"],
    "Instaladores": [".exe", ".msi", ".dmg"],
    "data": [".csv", ".json", ".xml"]
}

for file in downloads.iterdir():
    if file.is_file():
        ext = file.suffix.lower()

        for folder, extensions in folders.items():
            if ext in extensions:
                target_folder = downloads / folder
                target_folder.mkdir(exist_ok=True)

                shutil.move(str(file), str(target_folder / file.name))
                print(f"Movido {file.name} -> {folder}")
                break