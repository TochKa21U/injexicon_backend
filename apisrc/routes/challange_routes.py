from fastapi import Query, Request, APIRouter, Depends, status, WebSocket
from apisrc.auth.jwt import JWTGuard
from apisrc.challanges.challanges import submit_answer, submit_new_challange, submit_prompt, get_level_info, get_level_info_with_hint
from apisrc.challanges.challanges_dto import ChallangeSubmitAnswer, ChallangeSubmitNewLevel, ChallangeSubmitSecret, ChallangeRevealHints
from apisrc.auth.jwt import JWTGuard


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
    return get_level_info(levelcode=levelcode)

@router.post("/level/{levelcode}")
def get_level_with_hint(levelcode:str,payload:ChallangeRevealHints):
    """
    POST level by level code itself with specified hints
    "InputGuard": bool,
    "SanitizerGuard": bool,
    "LevelSecret": bool

    When it is marked as true, it will return with the given guard as well
    """
    return get_level_info_with_hint(levelcode=levelcode,payload=payload)

@router.post("/level")
def submit_newchallange(payload : ChallangeSubmitNewLevel,current_user: dict[str,str] = Depends(JWTGuard)):
    print(f"User info : {current_user}\nUser ID : {current_user.id}\nType : {type(current_user.id)}")
    return submit_new_challange(payload=payload,user_id=current_user.id)

@router.post("/levelsecret/{levelcode}")
def submit_secretcode(levelcode:str,secretcode:str):
    payload = ChallangeSubmitSecret(secretcode=prompt,levelcode=levelcode)
    return submit_answer(payload)

@router.post("/prompt")
def submit_to_warden(levelcode:str,prompt:str):
    payload = ChallangeSubmitAnswer(Prompt=prompt,levelcode=levelcode)
    return submit_prompt(payload=payload)