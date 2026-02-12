import boto3
from uuid import uuid4

S3_BUCKET = "fastapi-aws-gunjan-bucket"   # 🔴 replace with your bucket name
AWS_REGION = "ap-south-1"

s3 = boto3.client("s3", region_name=AWS_REGION)

def upload_file_to_s3(file):
    ext = file.filename.split(".")[-1]
    key = f"uploads/{uuid4()}.{ext}"

    s3.upload_fileobj(
        file.file,
        S3_BUCKET,
        key,
        ExtraArgs={"ContentType": file.content_type}
    )

    return f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{key}"
