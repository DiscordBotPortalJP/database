from sqlalchemy.orm import Session
from . import models, schemas


def get_bot(db: Session, user_id: int):
    return db.query(models.DiscordBot).filter(models.DiscordBot.user_id == user_id).first()


def get_bots(db: Session, skip: int = 0, limit: int = 5):
    return db.query(models.DiscordBot).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.DiscordBotCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.DiscordBot(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
