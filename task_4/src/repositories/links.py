from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.core.database import get_db
from src.models import LinkModel
from src.domain import Link
from src.core.logging import Logger
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

class Repository:
    '''
    НЕПРАВИЛЬНО. Оно работает все, но узнал только после сдачи, что я неправильно делал, нужно создавать сессию для каждого запроса, а не использовать общую.
    '''
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory
    
    async def create_link(self, link: Link):
        async with self.session_factory() as session:
            try:
                linkModel = LinkModel(original_url=link.original_url, short_code=link.short_code, clicks=link.clicks, created_at=link.created_at)
                session.add(linkModel)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise Exception(f"repo: create link: {e}")
    
    async def get_link_by_code(self, short_code:str) -> Link:
        async with self.session_factory() as session:
            try:

                stmt = select(LinkModel).filter_by(short_code=short_code)
                result = await session.execute(stmt)
                linkDB = result.scalar_one_or_none()

                if not linkDB: return None

                link = Link(id=linkDB.id,
                            original_url=linkDB.original_url,
                            short_code=linkDB.short_code,
                            clicks=linkDB.clicks,
                            created_at=linkDB.created_at)
                return link
            except Exception as e:
                await session.rollback()
                raise Exception(f"repo: get by code link: {e}")
    
    async def get_link_by_url(self, url:str) -> Link:
        async with self.session_factory() as session:
            try:

                stmt = select(LinkModel).filter_by(original_url=url)
                result = await session.execute(stmt)
                linkDB = result.scalar_one_or_none()

                if not linkDB: return None

                link = Link(id=linkDB.id,
                            original_url=linkDB.original_url,
                            short_code=linkDB.short_code,
                            clicks=linkDB.clicks,
                            created_at=linkDB.created_at)
                return link
            except Exception as e:
                await session.rollback()
                raise Exception(f"repo: get by url link: {e}")

    
    async def delete_link(self, short_code:str) -> Link:
        async with self.session_factory() as session:
            try:
                stmt = select(LinkModel).filter_by(short_code=short_code)
                result = await session.execute(stmt)
                linkDB = result.scalar_one_or_none()

                if not linkDB: return None
                
                await session.delete(linkDB)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise Exception(f"repo: delete link: {e}")

    async def update_clicks(self, short_code:str):
        async with self.session_factory() as session:
            try:
                stmt = select(LinkModel).filter_by(short_code=short_code)
                result = await session.execute(stmt)
                linkDB = result.scalar_one_or_none()

                if not linkDB: return None

                linkDB.clicks+=1
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise Exception(f"repo: update link: {e}")



def get_repo(session=Depends(get_db)):
    return Repository(session)