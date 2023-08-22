from fastapi import Query, Request, APIRouter, Depends, status, WebSocket
from apisrc.auth.jwt import JWTGuard
from apisrc.challanges.challanges import submit_answer, submit_new_challange, submit_prompt
from apisrc.challanges.challanges_dto import ChallangeSubmitAnswer, ChallangeSubmitNewLevel, ChallangeSubmitSecret


router = APIRouter()

@router.get("/protected-test")
def protected_test(current_user: dict[str,str] = Depends(JWTGuard)):
    print(f"UUID : {current_user.uuid}")
    return dict(current_user)

@router.get("/test")
def protected_test():
    return "Test on challanges endpoint"

# Submit new challange , submit answer, submit prompt

@router.get("/welcome/{leveltype}/{main}/{sub}")
def getwelcomelevel(leveltype:str,main:str,sub:int):
    """ 
    GET Default games from us. It is categorized under Leveltype , Main Level and Sub level
    They are : 
    Leveltype : warden , librarian
    Main : System, Input , Sanitizer - Warden ; Librarian,Technician,Disinformation - Librarian
    Sub : Level number from 1 to whatever is recommended
    """
    pass

@router.get("/level/{levelcode}")
def get_level(levelcode:str):
    """
    GET level by level code itself
    """
    pass

@router.post("/level")
def submit_newchallange():
    pass

@router.post("/levelsecret/{levelcode}")
def submit_secretcode(levelcode:str,secretcode:str):
    payload = ChallangeSubmitSecret(secretcode=prompt,levelcode=levelcode)
    return submit_answer(payload)

@router.post("/prompt")
def submit_to_warden(levelcode:str,prompt:str):
    payload = ChallangeSubmitAnswer(Prompt=prompt,levelcode=levelcode)
    return submit_prompt(payload=payload)