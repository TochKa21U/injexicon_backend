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