# FastAPI Guide

## Definition
FastAPI is a modern, fast (high-performance) web framework for building APIs with Python based on standard Python type hints. It allows you to build web APIs quickly and efficiently.

## Why Use FastAPI?
- **Super Fast!** 🚀 (Like a race car for coding)
- **Easy to Learn:** Write less, do more
- **Fast to Code:** Increase development speed by 200% to 300%
- **Great for APIs:** Ideal framework for creating APIs
- **Used by Big Companies:** Trusted by Netflix, Uber, and others
- **Asynchronous:** Efficiently handles multiple requests

## Create FastAPI using UV
### Steps
1. **Create a UV Project:**
```bash
uv init project_name
```

2. **Create Virtual Environment:**
```bash
python -m venv name
```

3. **Activate Environment:**
```bash
name/scripts/activate
```

4. **Install FastAPI Dependency:**
```bash
uv add fastapi
```

5. **Install psycopg2 for Database Connection:**
```bash
uv add psycopg2
```

6. **Run the Project:**
```bash
uv run fastapi dev main.py
```

## First Steps with FastAPI

### Basic Example
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

### Explanation
1. **Import FastAPI:**
```python
from fastapi import FastAPI
```

2. **Create FastAPI Instance:**
```python
app = FastAPI()
```

3. **Create a Path Operation:**
```python
@app.get("/")
```

4. **Define Path Operation Function:**
```python
async def root():
```

5. **Return Content:**
```python
return {"message": "Hello World"}
```

## Path Parameters
You can declare path "parameters" or "variables" with the same syntax used by Python format strings:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
```
- `item_id` is a path parameter passed to the function.

## Query Parameters
When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters
```python
@app.get("/items/")
async def read_item(name: str | None = None, q: str | None = None):
    if q:
        return {"name": name, "q": q}
    return {"name": name}
```
Example Request:
```
http://127.0.0.1:8000/items/?name="numan"&q="q"
```

## Request Body
When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
```python
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
