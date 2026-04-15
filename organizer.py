import os
import shutil
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

# Detecta automáticamente la carpeta Downloads
downloads = Path.home() / "Downloads"

folders = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Code": [".py", ".js", ".cs", ".java", ".html", ".css"],
    "Libros": [".epub", ".mobi"],
    "Instaladores": [".exe", ".msi", ".dmg"],
    "data": [".csv", ".json", ".xml"]
}

ext_to_folder = {
    ext: folder
    for folder, exts in folders.items()
    for ext in exts
}

for file in downloads.iterdir():
    if not file.is_file() or file.name.startswith("."):
        continue

    ext = file.suffix.lower()
    folder = ext_to_folder.get(ext)

    if not folder:
        continue

    target_folder = downloads / folder
    target_folder.mkdir(exist_ok=True)

    dest = target_folder / file.name

    if dest.exists():
        dest = target_folder / f"{file.stem}_copy{file.suffix}"

    try:
        shutil.move(str(file), str(dest))
        logging.info(f"Movido {file.name} -> {folder}")
    except Exception as e:
        logging.error(f"Error con {file.name}: {e}")