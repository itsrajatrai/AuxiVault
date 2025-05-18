from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

def get_current_user(db: Session = Depends(get_db)):
    # Temporary dummy auth: get user with id=1
    user = db.query(models.User).filter(models.User.id == 1).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
#     # In a real application, you would use JWT or session-based authentication
#     # to get the current user from the request.
#     # This is just a placeholder for demonstration purposes.

