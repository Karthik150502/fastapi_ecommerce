import uuid

from sqlalchemy import Column, ForeignKey, String, Text, Numeric, DateTime, func, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    balance = Column(Numeric(10, 2), nullable=False, default=0.00)
    type = Column(String(10), nullable=False, default="user")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

