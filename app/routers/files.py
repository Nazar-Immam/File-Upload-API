from fastapi import APIRouter , UploadFile , File , HTTPException , status , Depends
from sqlalchemy.orm import Session
from ..config import MAX_FILE_SIZE , ALLOWED_CONTENT_TYPES
from app.services.file_service import generate_unique_filename , save_file_to_disk
from app import schemas , models , database

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

@router.post("/upload", response_model= schemas.FileResponse)
async def upload_file(file: UploadFile = File(...) , db : Session = Depends(database.get_db)):

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="File type not Allowed")

    contents = await file.read()
    
    if len(contents) > MAX_FILE_SIZE :
        raise HTTPException(status_code= status.HTTP_413_CONTENT_TOO_LARGE,
                            detail="File too large, compress it to be under 5mb !")
    
     # Reset file pointer
    file.file.seek(0)

    # Generate safe filename
    stored_filename = generate_unique_filename(file.filename)

    # Save file
    file_path = save_file_to_disk(file, stored_filename)

    # CREATE DB RECORD
    new_file = models.File(
        original_name=file.filename,
        stored_name=stored_filename,
        content_type=file.content_type,
        file_path=file_path,
        file_size=len(contents)
    )

    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return new_file