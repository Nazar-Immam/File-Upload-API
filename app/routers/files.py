from fastapi import APIRouter , UploadFile , File , HTTPException , status
from ..config import MAX_FILE_SIZE , ALLOWED_CONTENT_TYPES

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="File type not Allowed")

    contents = await file.read()
    
    if len(contents) > MAX_FILE_SIZE :
        raise HTTPException(status_code= status.HTTP_413_CONTENT_TOO_LARGE,
                            detail="File too large, compress it to be under 5mb !")

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "file_size": len(contents)
    }