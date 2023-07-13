from pydantic import BaseModel, EmailStr
from typing import List, Optional

class User(BaseModel) :
    name : str
    email : EmailStr
    password : str
    role_id : Optional[int] = 1
    address : Optional[str] = None
    city : str
    center : str
    nid : str
    phone_number : str
    verified : Optional[bool] = False

class City(BaseModel) :
    name : str

class Center(BaseModel) :
    name : str

class VerificationCode(BaseModel) :
    user_id : int
    code : int

class UserResponse(BaseModel) :
    id : int
    name : str
    email : EmailStr
    nid : str
    city : str
    verified : bool
    class Config :
        orm_mode = True

class Token(BaseModel) :
    access_token : str
    token_type : str

class TokenData(BaseModel) :
    id : int