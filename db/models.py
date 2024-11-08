import uuid

from sqlalchemy import Column, String, ForeignKey,  Text, Numeric, DateTime, func, JSON, Enum as SQLEnum, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum
Base = declarative_base()




class UserRole(Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    balance = Column(Numeric(10, 2), nullable=False, default=0.00)
    type = Column(SQLEnum(UserRole), nullable=False, default=UserRole.user)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())




class Product(Base):
    __tablename__ = 'products'
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    image = Column(String(100), nullable=True)
    description = Column(Text, nullable=False)
    price = Column(Numeric(10, 2), nullable=False, default=0.00)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    added_by = Column(UUID, ForeignKey('users.id'), nullable=False)
    sku = Column(Numeric(10), nullable=False, default=0)
    status = Column(Boolean, nullable=False, default=True)