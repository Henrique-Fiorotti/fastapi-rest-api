from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

users = [
    {"id": 1, "name": "Daniel", "age": 34, "mail": "daniel@gmail.com"},
    {"id": 2, "name": "Alice", "age": 19, "mail": "alice@gmail.com"}
    ]

class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    mail: str


class UserPost(BaseModel):
    name: str
    age: int
    mail: str
    password: str

@app.get("/")
def api():
    return{"message": "API Started"}

@app.get("/users", response_model= list[UserResponse])
def list_users():
    return users

@app.get("/user/{id}", response_model= UserResponse)
def get_user(id: int):
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
        
@app.post("/user", response_model=UserPost, status_code=status.HTTP_201_CREATED)
def post_user(usuario: UserPost):
    new_id = max(user["id"] for user in users) + 1

    new_user = {
        "id": new_id,
        "name": usuario.name,
        "age": usuario.age,
        "mail": usuario.mail,
        "password": usuario.password
    }

    if usuario.age < 18:
        raise HTTPException(status_code=422, detail="Age not permited")

    users.append(new_user)
    return new_user

@app.delete("/user/{id}")
def delete_user(id: int):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return
    raise HTTPException(status_code=404, detail="User not found")