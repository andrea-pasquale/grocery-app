from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello Grocery App!"}


@app.get("/inventory")
def inventory():
    return []
