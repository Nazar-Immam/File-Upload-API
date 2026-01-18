from fastapi import APIRouter , UploadFile , File , HTTPException

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "file_size": len(contents)
    }