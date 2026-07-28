from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    category: str | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    category: str | None

    model_config = {"from_attributes": True}
