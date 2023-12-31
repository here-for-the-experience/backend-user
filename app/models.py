from .database import Base
from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
    
class User(Base) :
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role_id = Column(Integer, nullable=False)
    address = Column(String)
    nid = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    verified = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))


class VerificationCode(Base) :
    __tablename__ = "verification_code_table"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    verification_code = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))