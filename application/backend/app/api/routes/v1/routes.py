from fastapi import APIRouter

from app.logic.auth import add_user

router = APIRouter()


@router.post("/registration")
async def registration(login: str, email: str, password: str):
    await add_user(login, email, password)
