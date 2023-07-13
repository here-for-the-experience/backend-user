from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import user, auth

from fastapi import Depends, status, APIRouter, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .database import get_db
from sqlalchemy.orm import Session
from .schemas import Token
from . import models, utils, oauth2

from fastapi import APIRouter, Depends, Form, HTTPException, Header
from .database import get_db
from . import models, schemas, utils
from sqlalchemy.orm import Session
from .oauth2 import get_current_user
from typing import List
from starlette.responses import JSONResponse
from random import randrange
from .utils import send_email, send_text, mobile_number_verification
from pydantic import EmailStr

app = FastAPI()

origins = [
    "http://dev.redevops.store",
    "http://redevops.store",
    "http://dev.api.redevops.store",
    "http://api.redevops.store",
    "http://dev.auth.redevops.store",
    "http://auth.redevops.store",
    "http://dev.admin.redevops.store",
    "http://admin.redevops.store",

    "https://dev.redevops.store",
    "https://redevops.store",
    "https://dev.api.redevops.store",
    "https://api.redevops.store",
    "https://dev.auth.redevops.store",
    "https://auth.redevops.store",
    "https://dev.admin.redevops.store",
    "https://admin.redevops.store",
    
    "http://localhost",
    "http://localhost:8001",
    "http://localhost:8004",
    "http://localhost:5173",

    "http://127.0.0.1",
    "http://127.0.0.1:8001",
    "http://127.0.0.1:8004",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router) # Include the user related routes
app.include_router(auth.router) # Include the auth related routes

# @app.get("/", tags=["Home"]) 
# def home() :
#     return { "message" : "Hello"}


# @app.post("/login", response_model = Token)
# def login_user(user_credentials : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)) :
#     user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
#     if user is None :
#         raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "User not found")
    
#     if not utils.verify_password(user_credentials.password, user.password) :
#         raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "User not found")
    
#     access_token = oauth2.create_access_token({ "id" : user.id, "role_id" : user.role_id })
#     return {
#         "access_token" : access_token,
#         "token_type" : "Bearer"
#     }



# @app.post("/create", response_model = schemas.UserResponse, status_code = 201)
# def create_user(user : schemas.User, db : Session = Depends(get_db)) :
#     user.password = utils.hash(user.password)
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     try :
#         db.commit()
#     except :
#         raise HTTPException( status_code = 400, detail = { "message" : "an user with the provided email already exists"})
#     db.refresh(new_user)
#     return new_user

# # @router.put("/update", status_code = 201, tags=["users"], response_model = schemas.UserResponse)
# # def update_user(password : str = Form(...), db : Session = Depends(get_db), token_data : dict = Depends(get_current_user)) :
# #     id = token_data.id
# #     user_query = db.query(models.User).filter(models.User.id == id)
# #     user = user_query.first()
# #     user.password = utils.hash(password)
# #     user_query.update({ 'email' : user.email, 'password' : user.password }, synchronize_session = False)
# #     db.commit()
# #     return user_query.first()
    
# @app.get("/profile", response_model = schemas.UserResponse, status_code = 200)

# def get_user(db : Session = Depends(get_db), token_data : dict = Depends(get_current_user)) :
    
#     user = db.query(models.User).filter(models.User.id == token_data.id).first()
#     return user

# @app.post("/forgot")
# async def forgot_password( email : str = Form(...), db : Session = Depends(get_db) ) :
#     global code
#     code = randrange(40000, 90000)
#     user = db.query(models.User).filter(models.User.email == email).first()
#     if user is None :
#         raise HTTPException(status_code = 500, detail = "User Not Found")
#     try :
#         send_text(user.phone_number, code)
#     except :
#         raise HTTPException(status_code = 500, detail = "Try Again A Few Moments Later")
#     return JSONResponse(status_code = 200, content = { "message": "Verification Code Sent successfully" })

# @app.post("/validate", status_code = 200) 
# def validate_code(code_from_user : int = Form(...)) :
#     try :
#         if code_from_user != code if code else 23527895614 :
#             raise HTTPException(status_code = 404, detail = { "message" : "Invalid Code Provided" })
#     except :
#             raise HTTPException(status_code = 404, detail = { "message" : "Invalid Code Provided" })
#     return { "message" : "Code validated successfully" }


