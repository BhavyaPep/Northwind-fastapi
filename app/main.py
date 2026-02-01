
from fastapi import FastAPI
from app.routers import orders

app = FastAPI(
    title="Northwind Sales API",
    version="0.1.0",
    description="FastAPI over Northwind SQLite: explore and query orders/sales."
)

# Routers
app.include_router(orders.router, prefix="/orders", tags=["orders"])

@app.get("/health")
def health():
    return {"status": "ok"}
