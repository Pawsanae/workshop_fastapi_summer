from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/todos")
async def get_todos():
    return [
        {"id": 1, "details": "first todo"},
        {"id": 2, "details": "second todo"},
        {"id": 3, "details": "third todo"},
    ]

@app.get("/counter")
async def get_counter():
    global counter
    counter += 1
    return {"message": f"Counter is {counter}"}

class Item(BaseModel):
    item_id: int
    name: str
    description: str | None = None
    price: float

class ItemDto(BaseModel):
    name: str
    description: str | None = None
    price: float

items: dict[int, Item] = {}
id = 0

@app.post("/items/", response_model=Item)
def create_item(item: ItemDto):
    global id
    id += 1
    
    items[id] = Item(item_id=id, name=item.name, description=item.description, price=item.price)
    return items[id]