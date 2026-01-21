from fastapi import FastAPI
from .routers import files
from app.database import engine
from app import models,schemas
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="File Upload API")

app.include_router(files.router)

@app.get("/")
def default():
    return {"message" : "api testing successfull"}