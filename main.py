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

@app.post("/items/", response_model=Item, tags=["items"])
def create_item(item: ItemDto):
    global id
    id += 1
    items[id] = Item(item_id=id, name=item.name, description=item.description, price=item.price)
    return items[id]

@app.get("/items/{item_id}", response_model=Item |dict, tags=["items"])
def read_item(item_id: int):
    return items.get(item_id, {"error": "Item not found"})

@app.put("/items/{item_id}", response_model=Item | dict, tags=["items"])
def update_item(item_id: int, item: ItemDto):
    if item_id not in items:
        return {"error": "Item not found"}
    items[item_id] = Item(item_id=item_id, name=item.name, description=item.description, price=item.price)
    return items[item_id]


@app.delete("/items/{item_id}", response_model=dict, tags=["items"])
def delete_item(item_id: int):
    if item_id not in items:
        return {"error": "Item not found"}
    del items[item_id]
    return {"message": "Item deleted"}

