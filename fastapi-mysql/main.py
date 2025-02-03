from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import shutil
import os
from database import SessionLocal
from models import MusicFile

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# DB 세션 생성 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 음악 파일 업로드

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    music_file = MusicFile(filename=file.filename, path=file_location)
    db.add(music_file)
    db.commit()
    db.refresh(music_file)

    return {"message": "File uploaded successfully!", "filename": file.filename, "filepath": file_location}

# 🔹 업로드된 파일 목록 조회
@app.get("/files/")
async def list_files(db: Session = Depends(get_db)):
    files = db.query(MusicFile).all()
    return [{"id": file.id, "filename": file.filename, "filepath": file.path} for file in files]
