from fastapi import Depends, HTTPException

from app.crud import schemas, crud
from app.crud.crud import *
from app.database import SessionLocal as session, get_db
from fastapi import APIRouter

router=APIRouter()
@router.get("/users/")
async def get_all_users(page:int=1,page_size:int=20,db: Session = Depends(get_db)):
    return get_users(db,page,page_size)

@router.get("/user/{user_id}")
async def get_single_user(user_id:int,db: Session = Depends(get_db)):
    return get_user_by_id(db,user_id)\

@router.get("/user/email/{email_id}")
async def get_email_user(email_id:str,db: Session = Depends(get_db)):
    return crud.get_user_by_email(db,email_id)

@router.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)