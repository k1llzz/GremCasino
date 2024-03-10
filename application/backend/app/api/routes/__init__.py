from fastapi import APIRouter

from app.api.routes.root.routes import router as admin_router

router = APIRouter()

router.include_router(admin_router, tags=["Admin"], prefix="/admin")
