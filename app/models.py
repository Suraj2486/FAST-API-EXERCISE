from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text
from .db import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable = False)
    age = Column(Integer, nullable = False)
    published = Column(Boolean, server_default = 'TRUE', nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default=text('now()'))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    pw = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)