from fastapi import Query, Request, APIRouter, Depends, status, WebSocket
from apisrc.auth.jwt import JWTGuard


router = APIRouter()

@router.get("/protected-test")
def protected_test(current_user: dict[str,str] = Depends(JWTGuard)):
    print(f"UUID : {current_user.uuid}")
    return dict(current_user)

@router.get("/test")
def protected_test():
    return "Test on challanges endpoint"