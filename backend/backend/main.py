from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Shopihub API"}

@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Mouse"}
    ]