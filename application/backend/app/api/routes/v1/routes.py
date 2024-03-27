from fastapi import APIRouter, Response, Depends
from app.models.Users import UserSafe
from app.db.tables.users import Users
from app.logic.auth import add_user, login_user
from app.logic.dependence import get_current_user
from app.logic.token import create_acces_token


router = APIRouter()


@router.post("/registration")
async def registration(login: str, email: str, password: str):
    await add_user(login, email, password)
    return {"message": "Пользователь успешно зарегистрирован"}


@router.post("/login")
async def login(response: Response, emalog: str, password: str):
    user = await login_user(emalog, password)
    access_token = create_acces_token({"sub": str(user.id)})
    response.set_cookie("casino_access_token", access_token, httponly=True)
    return {"message": "Пользователь успешно авторизован"}


@router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("casino_access_token")
    return {"message": "Пользователь вышел из системы"}


@router.get("/data")
async def data(current_user: Users = Depends(get_current_user)):
    return {"data": current_user}
