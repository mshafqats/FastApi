from sqlalchemy.orm import Session
from datetime import datetime
from app.users.models import User, UserActivity
from app.core.security import hash_password, verify_password

def create_user(db: Session, email: str, password: str):
    user = User(
        email=email,
        hashed_password=hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

def record_login(db: Session, user_id: int):
    activity = UserActivity(user_id=user_id)
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

def record_logout(db: Session, activity_id: int):
    activity = db.get(UserActivity, activity_id)
    activity.logout_at = datetime.utcnow()
    db.commit()
