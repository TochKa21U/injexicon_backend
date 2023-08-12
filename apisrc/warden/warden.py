# WARDEN WILL BE RESPONSIBLE FOR SERVICES SUCH AS CALLING FROM DATABASE TO INPUT GUARDS AND RUNNING IT ETC
# ADD DEBUGGER AS WELL, IN CASE USER WANTS TO REVEAL EACH GUARD, WE CAN ADD IT
# ONLY THING USER NEEDS TO DO IS INPUT HIS OWN TOKEN(API TOKEN)
from apisrc.db.models import ChallangeQuestion, ChallangeSubmission
from apisrc.db.CRUD import read, find_first
from apisrc.warden.warden_dto import GuardPromptsDTO,RunGuardsDTO, SubmissionDTO
from apisrc.warden.config import runAgent, submissionCheck
from pydantic import BaseModel
from typing import Optional

def GetAllGuards(levelcode : str):
    """Will get the Guards and return it as interface"""
    LevelDetail = find_first(ChallangeQuestion,filter_by={"levelcode":levelcode})
    if not LevelDetail:
        return None
    return GuardPromptsDTO(InputGuard=LevelDetail.InputGuard,SystemContext=LevelDetail.SystemContext,SanitizerGuard=LevelDetail.SanitizerGuard)

def PreparePayloadForWarden(user_input:str, levelcode : str) -> RunGuardsDTO:
    """Will be used when user question is present and guards are taken from it"""
    guards = GetAllGuards(levelcode=levelcode)
    return RunGuardsDTO(user_input=user_input,system_context=guards.SystemContext,sanitizer=guards.SanitizerGuard,input_guard=guards.InputGuard)

def checkLevelSubmission(payload : SubmissionDTO):
    return submissionCheck(secretphrase=payload.secretphrase,submission_input=payload.submission_input)

def AskToWarden(payload : RunGuardsDTO):
    return runAgent(user_input=payload.user_input,system_context=payload.system_context,sanitizer=payload.sanitizer,input_guard=payload.input_guard)