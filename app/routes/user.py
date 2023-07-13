from fastapi import APIRouter, Depends, Form, HTTPException, Header
from ..database import get_db
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..oauth2 import get_current_user
from typing import List
from starlette.responses import JSONResponse
from random import randrange
from ..utils import send_email, send_text, mobile_number_verification
from pydantic import EmailStr
router = APIRouter(
    prefix = "/users",
    tags = ["users"]
)

@router.post("/create", response_model = schemas.UserResponse, status_code = 201)
def create_user(user : schemas.User, db : Session = Depends(get_db)) :
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    try :
        db.commit()
    except :
        raise HTTPException( status_code = 400, detail = { "message" : "an user with the provided email already exists"})
    db.refresh(new_user)
    return new_user

# @router.put("/update", status_code = 201, tags=["users"], response_model = schemas.UserResponse)
# def update_user(password : str = Form(...), db : Session = Depends(get_db), token_data : dict = Depends(get_current_user)) :
#     id = token_data.id
#     user_query = db.query(models.User).filter(models.User.id == id)
#     user = user_query.first()
#     user.password = utils.hash(password)
#     user_query.update({ 'email' : user.email, 'password' : user.password }, synchronize_session = False)
#     db.commit()
#     return user_query.first()
    
@router.get("/profile", response_model = schemas.UserResponse, status_code = 200)

def get_user(db : Session = Depends(get_db), token_data : dict = Depends(get_current_user)) :
    
    user = db.query(models.User).filter(models.User.id == token_data.id).first()
    return user

@router.post("/forgot")
async def forgot_password( email : str = Form(...), db : Session = Depends(get_db) ) :
    global code
    code = randrange(40000, 90000)
    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None :
        raise HTTPException(status_code = 500, detail = "User Not Found")
    try :
        send_text(user.phone_number, code)
    except :
        raise HTTPException(status_code = 500, detail = "Try Again A Few Moments Later")
    return JSONResponse(status_code = 200, content = { "message": "Verification Code Sent successfully" })

@router.post("/validate", status_code = 200) 
def validate_code(code_from_user : int = Form(...)) :
    try :
        if code_from_user != code if code else 23527895614 :
            raise HTTPException(status_code = 404, detail = { "message" : "Invalid Code Provided" })
    except :
            raise HTTPException(status_code = 404, detail = { "message" : "Invalid Code Provided" })
    return { "message" : "Code validated successfully" }
