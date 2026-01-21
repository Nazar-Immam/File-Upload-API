import os
import uuid
from fastapi import UploadFile
from ..config import UPLOAD_DIR

os.makedirs(UPLOAD_DIR, exist_ok=True) #This ensures upload dir is there, and if not then it will create it

#Generate safe unique filenames

def generate_unique_filename(original_filename: str) -> str:
    ext = os.path.splitext(original_filename)[1]  # keeps .pdf, .png
    unique_name = f"{uuid.uuid4().hex}{ext}"
    return unique_name

def save_file_to_disk(file: UploadFile, filename: str) -> str:
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        while chunk := file.file.read(1024 * 1024):
            buffer.write(chunk)

    return file_path
