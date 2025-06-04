from src.domain import Link
from datetime import datetime

class MockLinkService:
    def __init__(self):
        self.storage = {}

    async def create_link(self, link: Link):
        short_code = "mock123"
        link.short_code = short_code
        link.clicks = 0
        self.storage[short_code] = link
        return short_code

    async def get_link(self, short_code: str):
        return self.storage.get(short_code)
    
    async def get_link_with_clicks(self, short_code: str):
        return self.storage.get(short_code)

    async def delete_link(self, short_code: str):
        return self.storage.pop(short_code, None) is not None
