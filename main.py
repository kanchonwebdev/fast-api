from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "product_name": "Jeans pant",
        "product_size": "Medium",
        "product_id": "p_01",
        "product_price": "320 USD"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
