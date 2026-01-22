from fastapi import APIRouter

from .example_router import fruit_router

# here comes the big momma router
main_router = APIRouter()

main_router.include_router(fruit_router, prefix="/fruit", tags=["fruit"])
