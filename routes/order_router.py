from fastapi import APIRouter, HTTPException, status
from api_schemas.order_schema import OrderCreate, OrderRead, OrderUpdate
from database import DB_dependency
from db_models.order_model import Order_DB
from datetime import datetime

order_router = APIRouter()


@order_router.post("/", response_model=OrderRead)
def create_order(order_data: OrderCreate, db: DB_dependency):
    time = datetime.now()
    order = Order_DB(
        items = order_data.items,
        placed_at = time
        status = 'Pending'
        total = 0
        adress = order_data.address,
        note = order_data.note,
    )
    db.add(order)
    db.commit()
    return order
