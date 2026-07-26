from fastapi import FastAPI

from app.database.database import engine

app = FastAPI()


@app.get("/")
def root():
    with engine.connect():
        pass

    return {"status": "connected"}
