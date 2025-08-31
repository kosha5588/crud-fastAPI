from fastapi import FastAPI
import uvicorn
from backend.handlers import handlers
from backend.db.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(handlers.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8088, reload=True)


