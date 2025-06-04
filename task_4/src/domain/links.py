from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Link:
    id: int
    original_url: str 
    short_code: str
    clicks: int
    created_at: datetime = field(default_factory=datetime.now)