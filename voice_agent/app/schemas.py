# app/schemas.py

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str