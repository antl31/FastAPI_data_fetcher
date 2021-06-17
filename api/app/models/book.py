from sqlalchemy import Column, String, Text

from . import Base, BaseModelMixin


class Book(Base, BaseModelMixin):
    __tablename__ = "book"

    primary_isbn10 = Column(String(32), index=True)
    primary_isbn13 = Column(String(32), index=True)
    publisher = Column(String(64))
    description = Column(Text)
