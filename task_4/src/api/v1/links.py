from fastapi import APIRouter, Depends, Response
from fastapi.responses import JSONResponse
from src.schemas import LinkIn, LinkOut
from src.services import LinkService, get_service
from src.domain import Link


LinkRouter = APIRouter(
    prefix="/api/v1/links",
    tags=["private_links"]
)

@LinkRouter.get("/health")
async def health():
    return {"status": "ok"} 

@LinkRouter.post("/")
async def create_chat(link: LinkIn, linkService: LinkService = Depends(get_service)):
    
    short_code = await linkService.create_link(link=Link(original_url=link.original_url))
  
    return JSONResponse({"short_code":short_code}, 201)

@LinkRouter.get("/{short_code}", response_model=LinkOut)
async def get_link(short_code: str, linkService: LinkService = Depends(get_service)):  
    link = await linkService.get_link(short_code)
    if not link:
        return Response(status_code=404)
    
    return link

@LinkRouter.delete("/{short_code}")
async def delete_link(short_code: str, linkService: LinkService = Depends(get_service)):
    response = await linkService.delete_link(short_code)
    if not response:
        return Response(status_code=404)
    
    return Response(status_code=204)

