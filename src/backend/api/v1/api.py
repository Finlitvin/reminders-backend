from fastapi import APIRouter

from .routers.reminder import router as reminder_router

router = APIRouter()


router.include_router(reminder_router, prefix="/reminder", tags=["Reminder"])
