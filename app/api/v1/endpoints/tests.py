from fastapi import APIRouter
from app.core.config import settings
from app.utils.logger import logger

router = APIRouter(
prefix="/test", tags=["Test"]
)

@router.get("/")
def test():
    logger.info("Service started")
    return {"message": f"Test: {settings.APP_NAME}"}