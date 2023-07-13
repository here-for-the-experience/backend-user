from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import user, auth

from fastapi import Depends, status, APIRouter, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .database import get_db
from sqlalchemy.orm import Session
from .schemas import Token
from . import models, utils, oauth2

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
# app.include_router(auth.router) # Include the auth related routes

# @app.get("/", tags=["Home"]) 
# def home() :
#     return { "message" : "Hello"}


@app.post("/login", response_model = Token)
def login_user(user_credentials : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)) :
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if user is None :
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "User not found")
    
    if not utils.verify_password(user_credentials.password, user.password) :
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "User not found")
    
    access_token = oauth2.create_access_token({ "id" : user.id, "role_id" : user.role_id })
    return {
        "access_token" : access_token,
        "token_type" : "Bearer"
    }


