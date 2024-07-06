from fastapi import APIRouter

from api.v1.endpoints.books import router as book_router
from api.v1.endpoints.languages import router as languages_router

router = APIRouter()
router.include_router(book_router)
router.include_router(languages_router)