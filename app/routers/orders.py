
from typing import List
from fastapi import APIRouter, HTTPException, Query
from app.schemas import Order
from app import crud

router = APIRouter()

@router.get("/", response_model=List[Order])
def list_orders(limit: int = Query(50, ge=1, le=200), offset: int = Query(0, ge=0)):
    """
    List orders with pagination.
    """
    return crud.list_orders(limit=limit, offset=offset)

@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int):
    """
    Retrieve a single order by OrderID.
    """
    row = crud.get_order_by_id(order_id)
    if not row:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return row
