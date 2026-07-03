from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class CourseCreate(BaseModel):
    title: str
    description: str


class Token(BaseModel):
    access_token: str
    token_type: str