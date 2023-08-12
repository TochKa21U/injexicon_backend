from pydantic import BaseModel
from typing import Optional

class SubmissionDTO(BaseModel):
    secretphrase:str
    submission_input:str

class RunGuardsDTO(BaseModel):
    user_input:str
    system_context:str
    sanitizer:str = None
    input_guard:str = None

class GuardPromptsDTO(BaseModel):
    InputGuard : Optional[str] # Input
    SystemContext : str # System 
    SanitizerGuard : Optional[str] # Output