from apisrc.auth.auth_dto import SignUpPayload, TokenData, DemoSignupPayload
from apisrc.auth.jwt import authenticate_user, create_jwt_token, return_decoded_token, get_user, get_password_hash
from apisrc.db.CRUD import find_first, create, update, upsert, update_if_exists, read
from apisrc.db.models import Users, Demo, MessageCounter
from apisrc.users.users_dto import UserSignIn
from fastapi import HTTPException, status, Depends
from jose import JWTError, jwt
from typing import Optional
import uuid

def find_user_by_email(email:str):
    return find_first(Users,filter_by={"email":email})

def sign_in(payload:SignUpPayload):
    # Check current user in DB
    # Will handle under create_jwt_token
    # Write to a table about X-CSFR token and keep track of it with sessions
    access_token = create_jwt_token(payload=payload)
    return {"access_token": access_token, "token_type": "bearer"}

def sign_up(payload:UserSignIn):
    # Check if required some prequsities
    newUser = Users(username=payload.username,hashed_password=get_password_hash(payload.hashed_password),email=payload.email)
    createdUser = create(Users,newUser)
    counterdemo = MessageCounter(user_id=createdUser.id)
    create(MessageCounter,counterdemo)


def get_current_user(token:str):
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = return_decoded_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=username)
    if user is None:
        raise credentials_exception
    return user

def check_total_message_left(userid:int):
    try:
        foundUsersMessageCounter = find_first(MessageCounter,filter_by={"user_id":userid})
        print(f"Found message table : {foundUsersMessageCounter}")
        if foundUsersMessageCounter == None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User is not Found",
            )
    # return UserInDB(username='example',email='example@example.com',full_name='exampleDOMAIN',disabled=False,hashed_password='hashedExamplePassword')
        return foundUsersMessageCounter
    except Exception as e:
        print(f"Exception occured on check total message\nException : {e}")
        return e


def allow_block_limit_for_message(userid:int):
    """Returns True if user has reached the message limit"""
    try:
        foundUsersMessageCounter = find_first(MessageCounter,filter_by={"user_id":userid})
        if(foundUsersMessageCounter.current_amount >= foundUsersMessageCounter.max_message):
            return True
        return False
    except Exception as e:
        print(f"Exception occured on check total message\nException : {e}")
        return e

def increment_message_usage(userid:int,incrementation:int=1):
    try:
        foundUsersMessageCounter = check_total_message_left(userid=userid)
        print(f"Found Message qoute : {foundUsersMessageCounter}")
        update(MessageCounter, foundUsersMessageCounter.id, {"current_amount": foundUsersMessageCounter.current_amount+incrementation})
        return True
    except Exception as e:
        print(f"Exception at Increment message usage.\n{e}")
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Server error on Message Counter",
            )