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

class ChallangeRevealHints(BaseModel):
    SystemContext: Optional[bool] # In case tips are required, or we want to reveal
    InputGuard: Optional[bool] # Some sort of guard
    SanitizerGuard: Optional[bool]

class ChallangeLevelPublic(BaseModel):
    LevelName: str
    LevelInformation: str | None = None
    levelcode: str
    SystemContext: Optional[str] # In case tips are required, or we want to reveal
    InputGuard: Optional[str] # Some sort of guard
    SanitizerGuard: Optional[str]
    LevelSecret: Optional[str] # We can also move this to front end parse data for extra vulnerability
    # It might be good challange for people who want to bypass or understand web security