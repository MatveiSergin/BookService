from crud.base_crud import BaseCRUD
from models.models import BooksORM


class BooksCRUD(BaseCRUD):
    orm_model = BooksORM
