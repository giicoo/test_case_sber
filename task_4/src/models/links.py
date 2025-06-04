from sqlalchemy import DateTime, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from datetime import datetime

class Base(AsyncAttrs, DeclarativeBase):
    pass

class LinkModel(Base):
    __tablename__ = "links"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str] = mapped_column(String(2048)) 
    short_code: Mapped[str] = mapped_column(String(8))
    clicks: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(DateTime()) # не использую default, потому что задается в domain