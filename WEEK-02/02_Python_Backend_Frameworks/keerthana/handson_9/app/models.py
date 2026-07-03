from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str
    is_active: bool = True


class Course(BaseModel):
    id: int
    title: str
    description: str