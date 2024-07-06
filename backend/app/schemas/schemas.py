from datetime import date

from pydantic import BaseModel
from typing import Optional

class IdField(BaseModel):
    id: int

class LanguageAdd(BaseModel):
    name: str

class LanguageBase(LanguageAdd, IdField):
    pass

class ResponseSchemas(IdField):
    ok: bool = True

class TagAdd(BaseModel):
    name: str

class GenreAdd(BaseModel):
    name: str
    description: Optional[str]

class AuthorAdd(BaseModel):
    name: str
    birth_date: date
    death_date: date | None
    biography: str

class PublisherAdd(BaseModel):
    name: str
    birth_date: date
    address: str
    contact_info: str

class BookAdd(BaseModel):
    title: str
    description: Optional[str]
    year: Optional[int]
    language: LanguageAdd
    author: AuthorAdd
    publisher: PublisherAdd
    tags: list[TagAdd]
    genres: list[GenreAdd]


