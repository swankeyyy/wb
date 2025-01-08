from fastapi import APIRouter

from app.settings import settings
from api.views import router as api_router

router = APIRouter(prefix=settings.API_ROUTER_PREFIX)
router.include_router(api_router)