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
