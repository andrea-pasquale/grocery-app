from fastapi import FastAPI
from app.api import inventory, products


app = FastAPI()
app.include_router(inventory.router)
app.include_router(products.router)


@app.get("/")
def root():
    return {"message": "Hello Grocery App"}
