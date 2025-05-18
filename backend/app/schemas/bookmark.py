from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class BookmarkBase(BaseModel):
    url: HttpUrl
    title: Optional[str] = None
    description: Optional[str] = None

class BookmarkCreate(BookmarkBase):
    pass  # Same as base, for clarity

class BookmarkOut(BookmarkBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
