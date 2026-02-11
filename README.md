# FastAPI User Management API

RESTful API built with **FastAPI** to manage users, focusing on clean code, backend best practices, and scalable architecture.

This project started as a simple CRUD implementation and is being **progressively improved**, simulating the natural evolution of a real-world backend application.

---

## Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn
- (Upcoming) JWT Authentication
- (Upcoming) Password hashing

---

## Features

- User CRUD operations
- Data validation with Pydantic
- Secure API responses using `response_model`
- Proper error handling with HTTPException
- Correct HTTP status codes (200, 201, 404, 409, etc.)
- Swagger and ReDoc automatic documentation

---

## Current Project Structure

```text
.
├── app/
│   └── main.py
├── requirements.txt
└── README.md

