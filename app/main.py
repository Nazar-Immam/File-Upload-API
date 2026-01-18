from fastapi import FastAPI
from .routers import files

app = FastAPI(title="File Upload API")

app.include_router(files.router)

@app.get("/")
def default():
    return {"message" : "api testing successfull"}