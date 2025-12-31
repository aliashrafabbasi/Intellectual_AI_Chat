from pydantic import BaseModel
from typing import List
from datetime import datetime

class Message(BaseModel):
    role:str
    content:str

class Chat_session(BaseModel):
        session_id:str
        message:List[Message]
        created_at:datetime

