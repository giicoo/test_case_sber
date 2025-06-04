from fastapi import APIRouter, Depends, Response
from fastapi.responses import RedirectResponse
from src.schemas import LinkIn, LinkOut
from src.services import LinkService, get_service
from src.domain import Link


PublicRouter = APIRouter(
    tags=["public_links"]
)

@PublicRouter.get("/{short_code}")
async def get_redirect(short_code: str, linkService: LinkService = Depends(get_service)):  
    url = await linkService.get_link_with_clicks(short_code)
    if not url:
        return Response(status_code=404)
    
    return RedirectResponse(url=url, status_code=302)