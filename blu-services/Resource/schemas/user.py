from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class LoginRequest(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True

class RegisterRequest(BaseModel):
    email: str
    username: str
    password: str

    class Config:
        from_attributes = True


class UpdateRequest(BaseModel):
    email: Optional[EmailStr]
    username: Optional[str]
    password: Optional[str]

    class Config:
        from_attributes = True
