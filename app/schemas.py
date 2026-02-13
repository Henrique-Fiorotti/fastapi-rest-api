from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional

class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    mail: str

class UserPost(BaseModel):
    name: str = Field(..., max_length=50)
    age: int = Field(..., ge=18, lt=110, min_length=1, max_length=3)
    mail: EmailStr
    password: str = Field(..., min_length=3)
    
    @field_validator("mail") # Email POST Validation
    @classmethod
    def validate_company_email(cls, value):
        if not value.endswith("@company.com"):
            raise ValueError("Email must be from domain @company.com")
        return value
    
class UserPut(BaseModel):
    name: str
    age: int
    mail: EmailStr
    password: str = Field(..., min_length=3)
    
    @field_validator("mail")
    @classmethod
    def validate_company_email(cls, value):
        if not value.endswith("@company.com"):
            raise ValueError("Email must be from domain @company.com")
        return value

class UserPatch(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(default=None, ge=18)
    mail: Optional[EmailStr] = None
    password: Optional[str] = Field(default=None, min_length=3)
    
    @field_validator("mail")
    @classmethod
    def validate_company_email(cls, value):
        if not value.endswith("@company.com"):
            raise ValueError("Email must be from domain @company.com")
        return value
    