from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.database import ModelORM

class AuthorsORM(ModelORM):
    __tablename__ = "authors"
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    birth_date: Mapped[date]
    depth_date: Mapped[date]
    biography: Mapped[str]

class PublishersORM(ModelORM):
    __tablename__ = "publishers"
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    birth_date: Mapped[date]
    address: Mapped[str]
    contact_info: Mapped[str]

class LanguagesORM(ModelORM):
    __tablename__ = "languages"
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

class GenresORM(ModelORM):
    __tablename__ = "genres"
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str]
    #books: Mapped[list["BooksORM"]] = relationship(back_populates="genres", secondary="association_books_genres")

class TagsORM(ModelORM):
    __tablename__ = "tags"
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    #books: Mapped[list["BooksORM"]] = relationship(back_populates="genres", secondary="association_books_tags")

class AssociationBooksTags(ModelORM):
    __tablename__ = "association_books_tags"
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete="CASCADE"), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)

class AssociationBooksGenres(ModelORM):
    __tablename__ = "association_books_genres"
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete="CASCADE"), primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True)

class BooksORM(ModelORM):
    __tablename__ = "books"
    title: Mapped[str]
    description: Mapped[str]
    language_id = mapped_column(ForeignKey(LanguagesORM.id, ondelete="CASCADE"))
    author_id = mapped_column(ForeignKey(AuthorsORM.id, ondelete="CASCADE"))
    publisher_id = mapped_column(ForeignKey(PublishersORM.id, ondelete="CASCADE"))
    year: Mapped[int]
    tags: Mapped[list["TagsORM"]] = relationship("TagsORM", secondary="association_books_tags")
    genres: Mapped[list["GenresORM"]] = relationship("GenresORM", secondary="association_books_genres")
