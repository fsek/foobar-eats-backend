from fastapi import APIRouter

from .foobar_router import foobar_router

from .example_router import fruit_router

# Add new routers here
main_router = APIRouter()

main_router.include_router(foobar_router, prefix="/foobar", tags=["foobar"])
# main_router.include_router(fruit_router, prefix="/fruit", tags=["fruit"])
