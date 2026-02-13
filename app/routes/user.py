from main import app
from services import users
from fastapi import HTTPException, status
from schemas import UserResponse, UserPost, UserPatch, UserPut

# Verify if API is Working (GET)
@app.get("/", status_code=status.HTTP_200_OK)
def api():
    return{"message": "API Started"}


# List of all users (GET)
@app.get("/users", response_model= list[UserResponse], status_code=status.HTTP_200_OK)
def list_users():
    return users


# Search for a specific user (GET)
@app.get("/user/{id}", response_model= UserResponse, status_code=status.HTTP_200_OK)
def get_user(id: int):
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


# Create a new user
@app.post("/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def post_user(usuario: UserPost):
    new_id = max(user["id"] for user in users) + 1

    new_user = {
        "id": new_id,
        "name": usuario.name,
        "age": usuario.age,
        "mail": usuario.mail,
        "password": usuario.password
    }

    for user in users:
        if user["mail"] == usuario.mail:
            raise HTTPException(status_code=409, detail="Email already exists")

    users.append(new_user)
    return new_user


# PUT user
@app.put("/user/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def put_user(id: int, usuario: UserPut):
    for user in users:
        if user["id"] == id:
            user["name"] = usuario.name
            user["age"] = usuario.age
            user["mail"] = usuario.mail
            user["password"] = usuario.password
            
            return user
    raise HTTPException(status_code=404, detail="User not found")
            

# Patch some requested informations in user
@app.patch("/user/{id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def patch_user(id: int, userPatch: UserPatch):
    
    for user in users:
        if user["id"] == id:
            if userPatch.name is not None:
                user["name"] = userPatch.name
            if userPatch.age is not None:
                if userPatch.age > 18:
                    user["age"] = userPatch.age
                else:
                    raise HTTPException(status_code=422, detail="Age not valid")
            if userPatch.mail is not None:
                user["mail"] = userPatch.mail
            if userPatch.password is not None:
                user["password"] = userPatch.password
            return user
    raise HTTPException(status_code=404, detail="User not found")
        
        
# Delete user
@app.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return
    raise HTTPException(status_code=404, detail="User not found")