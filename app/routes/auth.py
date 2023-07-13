from fastapi import Depends, status, APIRouter, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import get_db
from sqlalchemy.orm import Session
from ..schemas import Token
from .. import models, utils, oauth2

router = APIRouter( tags = ["Authentication"] )


@router.post("/login", response_model = Token)
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
