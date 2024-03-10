from fastapi import APIRouter

from app.api.routes.root.routes import router as admin_router
from app.api.routes.v1.routes import router as v1_router

router = APIRouter()

router.include_router(admin_router, tags=["Admin"], prefix="/admin")
router.include_router(admin_router, tags=["V1"], prefix="/v1")
