from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

@router.post("/items/")
async def create_item(item: Item):
    return item