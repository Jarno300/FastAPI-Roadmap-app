from sqlalchemy.orm import Session
from app.models.user import User

def list_users(db: Session) -> list[User]:
    return db.query(User).all()

def create_user(db: Session, email: str) -> User:
    new_user = User(email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user