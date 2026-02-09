from fastapi import Request, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import decode_token
from app.users.models import User
from app.core.config import settings

def get_current_user( request: Request, db: Session = Depends(get_db) ):
    token = request.cookies.get(settings.COOKIE_NAME)
    if not token:
        return None

    user_id = decode_token(token)
    if not user_id:
        return None

    return db.get(User, user_id)
