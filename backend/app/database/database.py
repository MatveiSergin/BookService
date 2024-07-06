from datetime import date

from dotenv import load_dotenv
from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from settings import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=settings.ENGINE_ECHO,
    pool_size=settings.ENGINE_POOL_SIZE,
)
class ModelORM(DeclarativeBase):
    id: Mapped[int] = mapped_column(autoincrement='auto', primary_key=True)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(ModelORM.metadata.drop_all)
        await conn.run_sync(ModelORM.metadata.create_all)

db_session = async_sessionmaker(engine, expire_on_commit=False)

class AuthorORM(ModelORM):
    __tablename__ = "authors"
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    birth_date: Mapped[date]
    depth_date: Mapped[date]
    biography: Mapped[str]

class PublisherORM(ModelORM):
    __tablename__ = "publishers"
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    birth_date: Mapped[date]
    address: Mapped[str]
    contact_info: Mapped[str]

class LanguagesORM(ModelORM):
    __tablename__ = "languages"
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

class GenreORM(ModelORM):
    __tablename__ = "genres"
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str]
    books: Mapped[list["BooksORM"]] = relationship(back_populates="genres", secondary="association_books_genres")

#class TagORM(ModelORM):
#    __tablename__ = "tags"
#    name: Mapped[str] = mapped_column(unique=True, nullable=False)

#class AssociationBookTag(ModelORM):
#    __tablename__ = "association_books_tags"
#    book_id = mapped_column(ForeignKey("books.id"), nullable=False)
#    tag_id = mapped_column(ForeignKey("tags.id"), nullable=False)

class AssociationBookGenre(ModelORM):
    __tablename__ = "association_books_genres"
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete="CASCADE"), primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True)

class BooksORM(ModelORM):
    __tablename__ = "books"
    title: Mapped[str]
    description: Mapped[str]
    language_id = mapped_column(ForeignKey(LanguagesORM.id, ondelete="CASCADE"))
    author_id = mapped_column(ForeignKey(AuthorORM.id, ondelete="CASCADE"))
    publisher_id = mapped_column(ForeignKey(PublisherORM.id, ondelete="CASCADE"))
    year: Mapped[int]
    #tags: Mapped[list["TagsORM"]] = relationship("TagORM", back_populates="books", secondary="association_books_tags")
    genres: Mapped[list["GenreORM"]] = relationship(back_populates="books", secondary="association_books_genres")
