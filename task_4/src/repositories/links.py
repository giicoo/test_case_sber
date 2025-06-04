from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.core.database import get_db
from src.models import LinkModel
from src.domain import Link
from src.core.logging import Logger

class Repository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_link(self, link: Link):
        try:
            linkModel = LinkModel(original_url=link.original_url, short_code=link.short_code, clicks=link.clicks, created_at=link.created_at)
            self.session.add(linkModel)
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise Exception(f"repo: update link: {e}")
    
    async def get_link_by_code(self, short_code:str) -> Link:
        try:

            stmt = select(LinkModel).filter_by(short_code=short_code)
            result = await self.session.execute(stmt)
            linkDB = result.scalar_one_or_none()

            link = Link(id=linkDB.id,
                        original_url=linkDB.original_url,
                        short_code=linkDB.short_code,
                        clicks=linkDB.clicks,
                        created_at=linkDB.created_at)
            return link
        except Exception as e:
            await self.session.rollback()
            raise Exception(f"repo: update link: {e}")
    
    async def get_link_by_url(self, url:str) -> Link:
        try:

            stmt = select(LinkModel).filter_by(original_url=url)
            result = await self.session.execute(stmt)
            linkDB = result.scalar_one_or_none()

            link = Link(id=linkDB.id,
                        original_url=linkDB.original_url,
                        short_code=linkDB.short_code,
                        clicks=linkDB.clicks,
                        created_at=linkDB.created_at)
            return link
        except Exception as e:
            await self.session.rollback()
            raise Exception(f"repo: update link: {e}")

    
    async def delete_link(self, short_code:str) -> Link:
        try:
            stmt = select(LinkModel).filter_by(short_code=short_code)
            result = await self.session.execute(stmt)
            linkDB = result.scalar_one_or_none()

            await self.session.delete(linkDB)
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise Exception(f"repo: update link: {e}")

    async def update_clicks(self, short_code:str):
        try:
            stmt = select(LinkModel).filter_by(short_code=short_code)
            result = await self.session.execute(stmt)
            linkDB = result.scalar_one_or_none()

            linkDB.clicks+=1
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise Exception(f"repo: update link: {e}")



def get_repo(session=Depends(get_db)):
    return Repository(session)