from fastapi import APIRouter
from src.api.v1.links import LinkRouter
from src.api.v1.public import PublicRouter

main_router = APIRouter()
main_router.include_router(LinkRouter)
main_router.include_router(PublicRouter)