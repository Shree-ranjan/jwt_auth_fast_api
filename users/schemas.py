from pydantic import BaseModel, EmailStr

class CreateUserRequest(BaseModel):
    name : str
    email : EmailStr
    location : str
    about : str
    password : str