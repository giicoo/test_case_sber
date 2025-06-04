from datetime import datetime
from pydantic import BaseModel

class LinkIn(BaseModel):
    original_url: str

class LinkOut(BaseModel):
    original_url: str
    clicks: int
    created_at: datetime