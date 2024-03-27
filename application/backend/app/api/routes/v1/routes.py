from fastapi import APIRouter

from app.logic.auth import add_user, check_code

router = APIRouter()


@router.post("/registration")
async def registration(login: str, email: str, password: str):
    await add_user(login, email, password)


@router.get("/check_code")
async def check_confirm_code(code: int, login: str):
    await check_code(code, login)

