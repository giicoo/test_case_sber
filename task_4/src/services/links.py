import random
import string
from fastapi import Depends
from src.repositories import Repository, get_repo
from src.domain import Link
from src.core.logging import Logger


class LinkService:
    def __init__(self, repository: Repository):
        self.repo = repository

    async def create_link(self, link: Link) -> str:
        try:
            linkDB = await self.repo.get_link_by_url(link.original_url)
            if linkDB:
                return linkDB.short_code
            
            chars = string.ascii_letters + string.digits

            """
            Для избежания коллизий:
            Максимум 3 раз генерируем short_code, проверяем наличие его в БД,
            если есть то генерируем еще раз, если нет то выходим
            """
            for _ in range(3):
                short_code = ''.join(random.choices(chars, k=8))

                codeDB = await self.repo.get_link_by_code(short_code)
                if not codeDB:
                    break

            link.short_code = short_code

            await self.repo.create_link(link)

            return short_code
        except Exception as e:
            Logger.error(f"service: create: {e}")

    async def get_link(self, short_code: str) -> Link:
        try:
            linkDB = await self.repo.get_link_by_code(short_code)
            return linkDB
        except Exception as e:
            Logger.error(f"service: get: {e}")
    
    async def get_link_with_clicks(self, short_code: str) -> str:
        try:
            linkDB = await self.repo.get_link_by_code(short_code)
            await self.repo.update_clicks(short_code)
            return linkDB.original_url
        except Exception as e:
            Logger.error(f"service: get with clicks: {e}")
    
    async def delete_link(self, short_code: str) -> str:
        try:
            linkDB = await self.repo.get_link_by_code(short_code)
            if not linkDB: 
                return None
            await self.repo.delete_link(short_code)
            return "success"
        except Exception as e:
            Logger.error(f"service: create: {e}")
    

def get_service(repo: Repository = Depends(get_repo)):
    return LinkService(repo)