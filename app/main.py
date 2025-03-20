from fastapi import FastAPI ,Depends,HTTPException
from sqlalchemy.orm import Session


# Absolute imports (no more relative import errors)
from app import crud
from app import models
from app import schemas
from app import database
# from app.models import User
# from app.schemas import UserCreate, UserOut
# from app.crud import create_user, get_users, get_user, delete_user
# from app.database import get_db
app=FastAPI()


# Create DB tables
models.Base.metadata.create_all(bind=database.engine)

# create user endpoint
@app.post("/users/",response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db:Session=Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db,user)

# Gel all the user 
@app.get("/users/",response_model=list[schemas.UserOut])
def get_all_users(skip:int=0,limit:int=10,db:Session=Depends(database.get_db)):
    return crud.get_all_users(db,skip,limit)

# Get user by ID

@app.get("/users/{user_id}",response_model=schemas.UserOut)
def read_user(user_id:int,db:Session=Depends(database.get_db)):
    user =crud.get_user(db,user_id)
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user

# Delet user by ID 
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    deleted_user = crud.delet_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

@app.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    updated_user = crud.update_user(db, user_id, user)  
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user 
