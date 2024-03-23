from fastapi import APIRouter, Response
from app.logic.auth import add_user, login_user
from app.logic.token import create_acces_token

router = APIRouter()


@router.post("/registration")
async def registration(login: str, email: str, password: str):
    await add_user(login, email, password)


@router.post("/login")
async def login(response: Response, emalog: str, password: str):
    user = await login_user(emalog, password)
    access_token = create_acces_token({"sub": user.id})
    response.set_cookie("casino_access_token", access_token)
    return access_token
