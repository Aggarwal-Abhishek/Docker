from typing import Optional
from pydantic import BaseModel


class Note(BaseModel):
    note_id: Optional[str] = '-1'
    
    title: str
    date: str
    text: str
    username: str
    color: str


