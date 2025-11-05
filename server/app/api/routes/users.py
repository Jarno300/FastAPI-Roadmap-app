from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user import UserCreate, UserOut
from app.repositories.user_repo import list_users, create_user

router = APIRouter()

@router.get("", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    return list_users(db)

@router.post("", response_model=UserOut, status_code=201)
def post_user(payload: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, payload.email)