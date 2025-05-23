from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from pydantic import BaseModel, EmailStr

bookmarks = relationship("Bookmark", back_populates="user")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)

