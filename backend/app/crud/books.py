from crud.base_crud import BaseCRUD
from database.database import BooksORM


class BooksCRUD(BaseCRUD):
    orm_model = BooksORM
