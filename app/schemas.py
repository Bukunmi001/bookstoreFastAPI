from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    isbn: str

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
