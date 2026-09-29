from passlib.context import CryptContext
from sqlalchemy import TIMESTAMP, Boolean, Column, Enum, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from app.db import Base
import enum


class UserRole(str, enum.Enum):
    USER = "User",
    TECHNICIAN = 'Technician',
    MANAGER = 'Manager',
    ADMIN = "ADMIN"


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    role = Column(Enum(UserRole), nullable = False, default = 'User')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
