# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice route creation, request validation, and CRUD operations with structured JSON data.

## 📝 Tasks

### 🛠️	Create Your First FastAPI Endpoints

#### Description
Start from the provided `starter-code.py` file and run a FastAPI app locally. Implement basic endpoints to confirm your server is running and returning JSON responses.

#### Requirements
Completed program should:

- Run with `uvicorn starter-code:app --reload`
- Implement `GET /` returning a welcome message as JSON
- Implement `GET /health` returning `{ "status": "ok" }`


### 🛠️	Implement Book CRUD Endpoints

#### Description
Build API routes to manage a small in-memory collection of books. Each book should have an `id`, `title`, `author`, and `year`.

#### Requirements
Completed program should:

- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return one book or a 404 error if not found
- Implement `POST /books` to add a new book with request body validation
- Implement `PUT /books/{book_id}` to update an existing book or return 404
- Implement `DELETE /books/{book_id}` to remove a book and return a confirmation message


### 🛠️	Add Filtering and Error Handling

#### Description
Improve your API by supporting query parameters and clear error responses.

#### Requirements
Completed program should:

- Support `GET /books?author=...` to filter books by author (case-insensitive)
- Return meaningful HTTP errors using `HTTPException`
- Validate that `year` is in a reasonable range (for example, 1450 to current year)
- Return consistent JSON responses for successful and error cases