from typing import Dict, Union, Optional
from datetime import datetime

from sqlmodel import Field, SQLModel
from sqlalchemy import JSON, TIMESTAMP, Column, func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
import uuid


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    uuid: Optional[str] = Field(default=str(uuid.uuid4()))
    username: str
    hashed_password: str
    email: str | None = Field(...,unique=True)
    disabled: bool | None = None

class Demo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    userid: str
    hashed_password: str

class MessageCounter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    max_message: int = Field(default=100)
    current_amount : int = Field(default=0)

class ChallangeQuestion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="users.id") # User Assoicated ID to find who has posted
    LevelName : str = Field()
    SystemContext : str = Field()
    InputGuard : Optional[str]
    SanitizerGuard : Optional[str]
    LevelInformation : Optional[str] # Information that would be displayed to user about level
    TotalSubmitted : int = Field(default=0) # Amount of Submission in total
    levelcode: str = Field(default=str(uuid.uuid4()),unique=True)
    levelsecret : str = Field() # Level Secret Phrase
    isApproved : bool = Field(default=False)

class ChallangeSubmission(SQLModel, table=True): # Will be used when user is registered and want to save the progress 
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, foreign_key="users.id") # User Assoicated ID to find who has posted
    challange_id: Optional[int] = Field(default=None, foreign_key="challangequestion.id") # Challange Assoicated ID to find which challange was it
    Prompt : str = Field()
