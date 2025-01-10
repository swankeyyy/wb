from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from starlette.responses import Response
from starlette import status


router = APIRouter(tags=["Article Store"])


# @router.get("/", summary="Get all Articles by Telegram ID", status_code=200)
# async def get_all_articles(response: Response, telegram_user_id: Optional[str] = Header(None)):
#     if telegram_user_id:
#         response.status = status.HTTP_200_OK
#         return {"ok":"ok"}
#     raise HTTPException(status_code=400, detail="Telegram ID is required")


@router.post("/{article}", summary="Get Article")
async def post_article(article: str, response: Response, telegram_user_id: Optional[str] = Header(None)):
    response.status = status.HTTP_200_OK
    return {"article": article}