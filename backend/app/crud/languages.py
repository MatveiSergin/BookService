from crud.base_crud import BaseCRUD
from database.database import LanguagesORM
from schemas.schemas import LanguageBase


class LanguagesCRUD(BaseCRUD):
    orm_model = LanguagesORM
    schemas_model = LanguageBase