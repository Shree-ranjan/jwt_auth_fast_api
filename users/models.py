from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from datetime import datetime

from core.database import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(255), unique=True, index=True)
    location = Column(String(255))
    about = Column(String(255))
    password = Column(String(100))
    created_at = Column(DateTime, nullable=False, server_default=func.now())