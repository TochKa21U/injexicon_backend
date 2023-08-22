# Will add the services, submitNewChallange, SubmitAnswer(Only For Users, Normal people can try it without signup)

from apisrc.challanges.challanges_dto import ChallangeSubmitAnswer, ChallangeSubmitNewLevel, ChallangeSubmitSecret, ChallangeLevelPublic, ChallangeRevealHints
from apisrc.db.CRUD import create,find_first
from apisrc.db.models import ChallangeQuestion
from apisrc.warden.warden import AskToWarden, PreparePayloadForWarden

def submit_new_challange(payload:ChallangeSubmitNewLevel,user_id:int):
    definedPayload = ChallangeQuestion(
        user_id=user_id,LevelName=payload.LevelName,SystemContext=payload.SystemContext,
        InputGuard=payload.InputGuard,SanitizerGuard=payload.SanitizerGuard,
        LevelInformation=payload.LevelInformation,levelsecret=payload.levelsecret
    )
    created_level = create(ChallangeQuestion,definedPayload)
    return created_level

def submit_prompt(payload:ChallangeSubmitAnswer):
    """Used when user sends a prompt to the LLM"""
    prepared_payload = PreparePayloadForWarden(payload.Prompt,payload.levelcode)
    answer = AskToWarden(prepared_payload)
    return answer

def submit_answer(payload: ChallangeSubmitSecret):
    """Used when user sends the level password"""
    foundLevel = find_first(ChallangeQuestion,filter_by={"levelcode":payload.levelcode})
    if not foundLevel:
        return {"Error":"Level is not found","status":404}
    # return foundLevel.levelcode == payload.levelcode # Return whether answer is correct
    # Note : This version is case sensitive means that if the alphabets are not inserted in correct case answer will return false
    # Alternative non case sensitive
    return foundLevel.levelsecret.lower() == payload.secretcode.lower()

def get_level_info(levelcode:str):
    foundLevel = find_first(ChallangeQuestion,filter_by={"levelcode":levelcode})
    if not foundLevel:
        return {"Error":"Level is not found","status":404}
    # Level is found, return public facing
    levelinfo = ChallangeLevelPublic(LevelName=foundLevel.LevelName,LevelInformation=foundLevel.LevelInformation,levelcode=foundLevel.levelcode)
    return levelinfo
    # We can also make this one vulnerable by sharing some of the Level guards info in the response as well

def get_level_info_with_hint(levelcode:str,payload:ChallangeRevealHints):
    foundLevel = find_first(ChallangeQuestion,filter_by={"levelcode":levelcode})
    if not foundLevel:
        return {"Error":"Level is not found","status":404}
    # Level is found and check for matching data
    # # Vodoo code time,
    # for i,v in enumerate(payload):
    #     print(f"Index {i} Value : {v}\nKey name : {v[0]} Bool : {v[1]}")
    # Vodoo Code
    level_dict = foundLevel.dict()  # Convert the SQLModel instance to a dictionary

    levelinfo_data = {
        "LevelName": level_dict["LevelName"],
        "LevelInformation": level_dict["LevelInformation"],
        "levelcode": level_dict["levelcode"]
    }

    # Dynamically add attributes if they are in the payload and set to True
    for key, value in payload:
        if value:
            levelinfo_data[key] = level_dict[key]

    levelinfo = ChallangeLevelPublic(**levelinfo_data)

    return levelinfo