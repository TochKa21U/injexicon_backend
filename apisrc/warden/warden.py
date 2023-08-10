# WARDEN WILL BE RESPONSIBLE FOR SERVICES SUCH AS CALLING FROM DATABASE TO INPUT GUARDS AND RUNNING IT ETC
# ADD DEBUGGER AS WELL, IN CASE USER WANTS TO REVEAL EACH GUARD, WE CAN ADD IT
# ONLY THING USER NEEDS TO DO IS INPUT HIS OWN TOKEN(API TOKEN)
from apisrc.db.models import ChallangeQuestion, ChallangeSubmission
from apisrc.db.CRUD import read, find_first
from pydantic import BaseModel
from typing import Optional

class GuardPromptsDTO(BaseModel):
    InputGuard : Optional[str] # Input
    SystemContext : str = Field() # System 
    SanitizerGuard : Optional[str] # Output

def GetAllGuards(levelcode : str):
    """Will get the Guards and return it as interface"""
    LevelDetail = find_first(ChallangeQuestion,filter_by={"levelcode":levelcode})
    if not LevelDetail:
        return None
    return GuardPromptsDTO(InputGuard=LevelDetail.InputGuard,SystemContext=LevelDetail.SystemContext,SanitizerGuard=LevelDetail.SanitizerGuard)
    