from fastapi import APIRouter

from crud.books import BooksCRUD
from database.database import BooksORM

router = APIRouter(prefix="/books")



@router.get("")
async def get_books():
    books = await BooksCRUD.get_all()
    return books