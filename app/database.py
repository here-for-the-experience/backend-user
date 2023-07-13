from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv
load_dotenv()

# Get the database URL from the environment variable
url = os.getenv("URL")
# Create the database engine
engine = create_engine(url)
# Create a base class for declarative models
SessionLocal = sessionmaker(autocommit = False, autoflush = True, bind = engine)
Base = declarative_base()

def get_db() :
    """
    Function to get a database session.
    """
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()