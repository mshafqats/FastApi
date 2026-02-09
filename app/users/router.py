from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.users import service, schemas
from app.core.security import create_token
from app.core.config import settings
from app.users.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup", response_model=schemas.UserResponse)
def signup(data: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, data.email, data.password)

@router.post("/login")
def login( data: schemas.UserCreate, response: Response, db: Session = Depends(get_db) ):
    user = service.authenticate_user(db, data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    activity = service.record_login(db, user.id)
    token = create_token(user.id)

    response.set_cookie( key=settings.COOKIE_NAME, value=token, httponly=True )
    response.set_cookie( key="activity_id", value=str(activity.id), httponly=True )
    return {"message": "Logged in"}

@router.post("/logout")
def logout( response: Response, db: Session = Depends(get_db), user=Depends(get_current_user) ):
    response.delete_cookie(settings.COOKIE_NAME)
    response.delete_cookie("activity_id")
    return {"message": "Logged out"}
