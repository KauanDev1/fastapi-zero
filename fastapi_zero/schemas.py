from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    email: str  # EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: str  # EmailStr
    id: int


class UserDB(UserSchema):
    id: int

    