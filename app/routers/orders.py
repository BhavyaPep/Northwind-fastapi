
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_orders_placeholder():
    return {"message": "orders endpoint coming up"}
