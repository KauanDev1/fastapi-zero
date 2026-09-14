from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    username: str
    email: str #EmailStr
    password: str

