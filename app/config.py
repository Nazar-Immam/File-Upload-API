import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR= os.path.join(BASE_DIR , "uploads")


MAX_FILE_SIZE = 5*1024*1024 # =5mb

ALLOWED_CONTENT_TYPES = {  
    "image/png",       #Specifc MIME Types
    "image/jpeg",
    "application/pdf"
}