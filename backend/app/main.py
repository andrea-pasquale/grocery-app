from fastapi import FastAPI
from app.api import inventory, products
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(inventory.router)
app.include_router(products.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello Grocery App"}
