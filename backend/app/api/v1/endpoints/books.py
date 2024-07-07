from fastapi import APIRouter

from crud.books import BooksCRUD

router = APIRouter(prefix="/books")



@router.get("")
async def get_books():
    books = await BooksCRUD.get_all()
    return books