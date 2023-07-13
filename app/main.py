from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import user, auth
from . import models, database

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Home"]) 
def home() :
    return { "message" : "Hello"}

app.include_router(user.router) # Include the user related routes
app.include_router(auth.router) # Include the auth related routes
