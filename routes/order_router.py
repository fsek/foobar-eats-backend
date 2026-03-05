from fastapi import APIRouter, HTTPException, status
from api_schemas.order_schema import OrderCreate, OrderRead, OrderUpdate
from database import DB_dependency
from db_models.order_model import Order_DB
from datetime import datetime

order_router = APIRouter()


# Hello Hello
@order_router.post("/", response_model=OrderRead)
def create_order(order_data: OrderCreate, db: DB_dependency):
    order = Order_DB(
        items=order_data.items,
        placed_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        status="pending",
        total=0,
        address=order_data.address,
        note=order_data.note,
    )
    db.add(order)
    db.commit()
    db.refresh(order)  # Refresh to get the generated ID and any defaults
    return order


@order_router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, db: DB_dependency):
    order = db.query(Order_DB).filter_by(id=order_id).one_or_none()
    if order is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return order


@order_router.get("/", response_model=list[OrderRead])
def get_all_orders(db: DB_dependency):
    orders = db.query(Order_DB).all()
    return orders


@order_router.delete("/{order_id}", response_model=OrderRead)
def delete_order(order_id: int, db: DB_dependency):
    order = db.query(Order_DB).filter_by(id=order_id).one_or_none()
    if order is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    db.delete(order)
    db.commit()
    return order


@order_router.patch("/{order_id}", response_model=OrderRead)
def update_order(order_id: int, order_data: OrderUpdate, db: DB_dependency):
    order = db.query(Order_DB).filter_by(id=order_id).one_or_none()
    if order is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)

    # This does not allow one to "unset" values that could be null but aren't currently
    for var, value in vars(order_data).items():
        if value is not None:
            setattr(order, var, value)

    db.commit()
    return order
