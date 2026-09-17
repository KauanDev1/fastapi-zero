from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: str #EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: str #EmailStr
    id: int


class UserDB(UserSchema):
    id: int


