from pydantic import BaseModel
from datetime import datetime

class FileResponse(BaseModel):
    id: int
    original_name: str
    stored_name: str
    content_type: str
    file_size: int
    created_at: datetime

    class Config:
        from_attributes = True
