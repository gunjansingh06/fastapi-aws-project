from fastapi import APIRouter, UploadFile, File
from app.s3_utils import upload_file_to_s3

router = APIRouter(prefix="/upload", tags=["S3 Upload"])

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_url = upload_file_to_s3(file)
    return {
        "message": "File uploaded successfully",
        "file_url": file_url
    }
