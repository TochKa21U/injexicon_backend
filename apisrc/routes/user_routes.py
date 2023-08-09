from fastapi import Query, Request, APIRouter, Depends
from fastapi.responses import RedirectResponse
from apisrc.users.users import sign_in, sign_up, check_total_message_left, increment_message_usage
from apisrc.auth.auth_dto import SignUpPayload, DemoSignupPayload
from apisrc.users.users_dto import UserSignIn
from apisrc.auth.jwt import JWTGuard
from typing import Optional
import os

router = APIRouter()

@router.get("/test")
def getDemoTest()-> dict:
    return {"message": "Hello World"}

@router.get("/protected-test")
async def protected_test(current_user: dict[str,str] = Depends(JWTGuard)):
    print(f"Current user id : {current_user.id}")
    return {"message": "Protected Hello World"} 

@router.post("/signin")
async def users_signin(payload: SignUpPayload):
    return sign_in(payload)

@router.post("/signup")
async def user_signup(payload:UserSignIn):
    sign_up(payload=payload)
    return {"message": "Registration has been succesful"} 

@router.get("/messagecount")
def getTotalMessageleft(current_user: dict[str,str] = Depends(JWTGuard)):
    print(f"Current user id : {current_user.id}")
    return check_total_message_left(userid=current_user.id)

# Testing purposes DO NOT USE IT IN THE PROD
@router.get("/messagecountincr")
def getTotalMessageleft(current_user: dict[str,str] = Depends(JWTGuard)):
    print(f"Current user id : {current_user.id}")
    return increment_message_usage(userid=current_user.id,incrementation=5)