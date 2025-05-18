from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.bookmark import Bookmark
from app.schemas.bookmark import BookmarkCreate, BookmarkOut
from typing import List
from app.database import get_db
from app.dependencies import get_current_user

router = APIRouter(prefix="/bookmarks", tags=["bookmarks"])

@router.post("/", response_model=BookmarkOut)
def create_bookmark(bookmark: BookmarkCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_bookmark = models.Bookmark(user_id=current_user.id, **bookmark.dict())
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)
    return db_bookmark

@router.get("/", response_model=List[BookmarkOut])
def list_bookmarks(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(Bookmark).filter(Bookmark.user_id == current_user.id).all()

@router.get("/{bookmark_id}", response_model=BookmarkOut)
def get_bookmark(bookmark_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id,Bookmark.user_id == current_user.id).first()
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    return bookmark

@router.put("/{bookmark_id}", response_model=BookmarkOut)
def update_bookmark(bookmark_id: int, bookmark_update: BookmarkCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id, Bookmark.user_id == current_user.id).first()
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    for key, value in bookmark_update.dict(exclude_unset=True).items():
        setattr(bookmark, key, value)
    db.commit()
    db.refresh(bookmark)
    return bookmark

@router.delete("/{bookmark_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_bookmark(bookmark_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    bookmark = db.query(Bookmark).filter(Bookmark.id == bookmark_id, Bookmark.user_id == current_user.id).first()
    if not bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    db.delete(bookmark)
    db.commit()
    return
