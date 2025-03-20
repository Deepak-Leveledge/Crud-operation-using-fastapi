from sqlalchemy.orm import Session
from .import models,schemas



# Create a new user
def create_user(db:Session,user:schemas.UserCreate):
    db_user=models.User(
        username=user.username,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Get a user by ID
def get_user(db:Session,user_id:int):
    return db.query(models.User).filter(models.User.id==user_id).first()

# get all the user 
def get_all_users(db:Session,skip:int=0,limit:int=10):
    return db.query(models.User).offset(skip).limit(limit).all()


# delete the user 
def delet_user(db:Session,user_id:int):
    db_user=db.query(models.User).filter(models.User.id==user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None

# update the user
def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db_user.password = user.password
        db.commit()
        db.refresh(db_user)
        return db_user  
    return None

        