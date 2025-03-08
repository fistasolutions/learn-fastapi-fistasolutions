from fastapi import FastAPI
from requestbody import router as requestbody_router

app = FastAPI()


app.include_router(requestbody_router)

# First Steps
@app.get("/")
async def root():
    return {"message": "Hello World"}



# Path Parameters
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# Query Parameters
@app.get("/items/")
async def read_item(name:str | None = None, q: str | None = None):
    if q:
        return {"name": name, "q": q}
    return {"name": name}