from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

users = [
    {"id": 1, "name": "Daniel", "email": "daniel@gmail.com"},
    {"id": 2, "name": "Alice", "email": "alice@gmail.com"}
    ]

@app.get("/")
def api():
    return{"message": "API Started"}

@app.get("/users")
def list_users():
    return users

@app.delete("/user/{id}")
def delete_user(id: int):
    for user in users:
        if user["id"] == id:
            users.remove(user)