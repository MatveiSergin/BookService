
from database.database import LanguagesORM

from crud.languages import LanguagesCRUD
from schemas.schemas import LanguageAdd


async def init_data():
    language: LanguageAdd = LanguageAdd(name='English')
    await LanguagesCRUD.add_one(language)