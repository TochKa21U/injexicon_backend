from pydantic import BaseModel
from typing import Optional

class ChallangeSubmitNewLevel(BaseModel):
    LevelName: str
    PromptGuard: str
    LevelInformation: str | None = None

class ChallangeSubmitAnswer(BaseModel):
    Prompt : str