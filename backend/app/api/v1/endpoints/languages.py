from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request
from crud.languages import LanguagesCRUD
from schemas.schemas import LanguageBase, LanguageAdd, ResponseSchemas

router = APIRouter(prefix="/languages")


@router.get("/all")
async def get_languages(request: Request) -> list[LanguageBase]:
    languages = await LanguagesCRUD.get_all()
    return languages

@router.get("/{language_id}")
async def get_language(request: Request, language_id: int) -> LanguageBase:
    language = await LanguagesCRUD.get_by_id(language_id)

    if not language:
        raise HTTPException(status_code=404, detail="Language not found")
    return language

@router.post("/add")
async def add_language(
        language: Annotated[LanguageAdd, Depends()]
) -> ResponseSchemas:
    language_id = await LanguagesCRUD.add_one(language)
    response = ResponseSchemas(id=language_id)
    return response

@router.delete("/{language_id}")
async def delete_language(language_id: int) -> ResponseSchemas:
    await LanguagesCRUD.delete_one(language_id)
    return ResponseSchemas(ok=True, id=language_id)