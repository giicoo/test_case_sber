from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Link:
    id: int = 0
    original_url: str = None
    short_code: str = None
    clicks: int = 0
    created_at: datetime = field(default_factory=datetime.now)