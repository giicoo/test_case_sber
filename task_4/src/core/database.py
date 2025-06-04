from fastapi import Request
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from src.core.logging import Logger
from src.models.links import Base
from src.core.environment import DB_URL


async def connect_to_db():
    engine = create_async_engine(DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    AsyncSession = async_sessionmaker(bind=engine)
    session = AsyncSession()
    Logger.info("DB connected")
    return session

async def close_db_connection(session: AsyncSession):
    await session.close()
    Logger.info("DB connection closed")

def get_db(request: Request)-> AsyncSession:
    return request.app.state.db_session
