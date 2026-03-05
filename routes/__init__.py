from fastapi import APIRouter

from .example_router import fruit_router
from .menu_router import menu_router
from .order_router import order_router

# Add new routers here
main_router = APIRouter()

main_router.include_router(fruit_router, prefix="/fruit", tags=["fruit"])
main_router.include_router(menu_router, prefix="/menu", tags=["menu"])
main_router.include_router(order_router, prefix="/order", tags=["order"])
