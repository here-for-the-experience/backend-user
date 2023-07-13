from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import user, auth
from . import models, database

app = FastAPI()

origins = [
    "http://dev.redevops.store",
    "http://redevops.store",
    "http://dev.api.redevops.store",
    "http://api.redevops.store",
    "http://dev.auth.redevops.store",
    "http://auth.redevops.store",

    "https://dev.redevops.store",
    "https://redevops.store",
    "https://dev.api.redevops.store",
    "https://api.redevops.store",
    "https://dev.auth.redevops.store",
    "https://auth.redevops.store",
    
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