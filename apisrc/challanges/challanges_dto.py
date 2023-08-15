from pydantic import BaseModel
from typing import Optional

class ChallangeSubmitNewLevel(BaseModel):
    LevelName: str
    LevelInformation: str | None = None
    SystemContext : str # AKA prompt guard
    InputGuard : Optional[str]
    SanitizerGuard : Optional[str]
    levelsecret : str # Level Secret Phrase

class ChallangeSubmitAnswer(BaseModel):
    Prompt : str
    levelcode: str

class ChallangeSubmitSecret(BaseModel):
    secretcode : str
    levelcode : str