# routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.models.user import User
from app.utils.security import hash_password
from app.database import get_db
from passlib.context import CryptContext

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter((User.email == user.email) | (User.username == user.username)).first()
    if existing:
        raise HTTPException(status_code=400, detail="User with that email or username already exists.")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login")
def login(user_cred: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_cred.email).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not pwd_context.verify(user_cred.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {"message": "Login successful", "user_id": user.id}

@router.get("/me", response_model=UserOut)
def get_current_user(db: Session = Depends(get_db), user: User = Depends(get_db)):
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user
