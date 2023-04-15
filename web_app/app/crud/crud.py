from sqlalchemy.orm import Session
from . import models,schemas

def get_user_by_id(db:Session,user_id:int):
    """
The get_user_by_id function takes in a user_id and returns the User object with that id.
If no such user exists, it will return None.

:param db:Session: Pass the database session into the function
:param user_id:int: Specify the type of data that will be passed into the function
:return: A user object
:doc-author: prabhakarant
"""
    return db.query(models.User).filter(models.User.id==user_id).first()

def get_user_by_email(db:Session,email:str):
    """
The get_user_by_email function takes in a database session and an email address,
and returns the user object associated with that email address. If no such user exists,
it returns None.

:param db:Session: Connect to the database
:param email:str: Specify the type of data that is being passed into the function
:return: A user object
:doc-author: prabhakarant
"""
    print(email)
    return db.query(models.User).filter(models.User.email==email).first()
def get_users(db:Session, page:int = 1, page_size:int=20):
    """
The get_users function returns a list of users from the database.


:param db:Session: Pass the database session to the function
:param page:int: Specify the page number to return
:param page_size:int: Determine the number of users that are returned per page
:return: A list of users
:doc-author: prabhakarant
"""
    offset=(page-1)*page_size
    limit=page*page_size
    return db.query(models.User).offset(offset).limit(limit).all()

def create_user(db:Session,user:schemas.UserCreate):
    """
The create_user function creates a new user in the database.
    Args:
        db (Session): The database session object.
        user (UserCreate): The UserCreate model to be created in the database.

:param db:Session: Create a session with the database
:param user:UserCreate: Create a new user object
:return: The user object that was created
:doc-author: prabhakarant
"""
    password='***'+user.password+"####" ####Can be hashed in actual code
    db_user=models.User(email=user.email,password=password,address=user.address,first_name=user.first_name,last_name=user.last_name,city=user.city,state=user.state,pincode=user.pincode,is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user