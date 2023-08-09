from pydantic import BaseModel
from typing import Optional

class UserSignIn(BaseModel):
    username: str
    hashed_password: str
    email: str | None = None


class UserPublic(BaseModel):
    email: str
    id: int
    username: str