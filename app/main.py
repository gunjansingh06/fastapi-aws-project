from fastapi import FastAPI
from app.routes import notes, upload   # 🔴 add upload
from app.models import Base
from app.database import engine

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# 🔴 register both routers
app.include_router(notes.router)
app.include_router(upload.router)

@app.get("/")
def root():
    return {"message": "FastAPI is running"}
