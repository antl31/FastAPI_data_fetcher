from pydantic import BaseModel, validator

from . import DefaultResponse


class BookSchema(BaseModel):
    primary_isbn10: str
    primary_isbn13: str
    publisher: str
    description: str

    class Config:
        orm_mode = True
        extra = "ignore"

    @validator("description")
    def validate(cls, value: str):
        assert len(value) < 1000, " too long description"
        return value

    def __hash__(self):
        return hash(f"{self.primary_isbn10}_{self.primary_isbn13}")

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return (self.primary_isbn10 == other.primary_isbn10) and (
                self.primary_isbn13 == other.primary_isbn13
            )
        return NotImplemented


class BookOutputSchema(DefaultResponse):
    data: list[BookSchema]
