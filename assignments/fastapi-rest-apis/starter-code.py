from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    author: str = Field(min_length=1, max_length=80)
    year: int = Field(ge=1450, le=datetime.now().year)


class Book(BookInput):
    id: int


# In-memory data store for the assignment.
books: list[Book] = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937),
    Book(id=2, title="Pride and Prejudice", author="Jane Austen", year=1813),
]


@app.get("/")
def root() -> dict[str, str]:
    # TODO: Return a welcome message as JSON.
    return {"message": "Welcome to the Books API"}


@app.get("/health")
def health() -> dict[str, str]:
    # TODO: Return {"status": "ok"}.
    return {"status": "ok"}


@app.get("/books")
def list_books(author: Optional[str] = Query(default=None)) -> list[Book]:
    # TODO: If author is provided, filter by author name (case-insensitive).
    if not author:
        return books

    return [book for book in books if author.lower() in book.author.lower()]


@app.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    # TODO: Return matching book or raise HTTPException(status_code=404).
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201)
def create_book(payload: BookInput) -> Book:
    # TODO: Create a new book with a new ID and append to books.
    next_id = max((book.id for book in books), default=0) + 1
    new_book = Book(id=next_id, **payload.model_dump())
    books.append(new_book)
    return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, payload: BookInput) -> Book:
    # TODO: Update an existing book by ID or return 404.
    for index, book in enumerate(books):
        if book.id == book_id:
            updated = Book(id=book_id, **payload.model_dump())
            books[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict[str, str]:
    # TODO: Remove matching book and return a JSON confirmation message.
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {"message": f"Book {book_id} deleted"}
    raise HTTPException(status_code=404, detail="Book not found")