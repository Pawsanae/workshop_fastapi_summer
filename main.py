from fastapi import FastAPI

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

