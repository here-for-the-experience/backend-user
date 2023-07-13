from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel) :
    name : str
    email : EmailStr
    password : str
    role_id : Optional[int] = 1
    address : Optional[str] = None
    nid : str
    phone_number : str
    verified : Optional[bool] = True


class VerificationCode(BaseModel) :
    user_id : int
    code : int

class UserResponse(BaseModel) :
    id : int
    name : str
    email : EmailStr
    nid : str
    verified : bool
    class Config :
        orm_mode = True

class Token(BaseModel) :
    access_token : str
    token_type : str

class TokenData(BaseModel) :
    id : int
    role_id: int