# Importation
from fastapi import FastAPI

# Iniciatializing FastAPI
app = FastAPI()

#Alteração teste

# Search for a specific user (GET)
@app.get("/user/{id}", response_model= UserResponse, status_code=status.HTTP_200_OK)
def get_user(id: int):
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Search for a specific user (GET)
@app.get("/user/{id}", response_model= UserResponse, status_code=status.HTTP_200_OK)
def get_user(id: int):
    for user in users:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")