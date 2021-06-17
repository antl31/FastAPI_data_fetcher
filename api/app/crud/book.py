from sqlalchemy.orm import Session
from fastapi import Depends

from api.app.models.book import Book
from api.app.database import get_db
from api.app.schemas.book import BookSchema

from . import BaseDAO


class BookDAO(BaseDAO):
    def __init__(self, db: Session = Depends(get_db)):
        super().__init__(db)
        self.model = Book

    def create(self, book_schema: BookSchema):
        # create book
        book = Book(**book_schema.dict())
        self.db.add(book)
        return book

    def get_by_ids(self, ids: tuple):
        return self.db.query(self.model).filter(self.model.primary_isbn10.in_(ids))

    def create_all(self, books: [BookSchema]):
        # create list of books
        books = set(books)
        all_ids = [d.primary_isbn10 for d in books]
        found = [d.primary_isbn10 for d in self.get_by_ids(tuple(all_ids)).all()]
        books_insert = [
            Book(**d.dict()) for d in books if d.primary_isbn10 not in found
        ]
        self.db.add_all(books_insert)
        return books_insert
