from datetime import datetime
from fastapi import Request, Depends
from app.exceptions.api import ClientErrorApiException
from jose import jwt, JWTError
from app.logic.auth import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("casino_access_token")
    if not token:
        raise ClientErrorApiException(
            status_code=401,
            detail={"message": "Токен отсутствует"},
        )
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, "L2QMijyRgXKo4mjG8N7NQKGqilWko/V8xRaVBjXlgAw=", "HS256")
    except JWTError:
        raise ClientErrorApiException(
            status_code=401,
            detail={"message": "Токен не является jwt"},
        )
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise ClientErrorApiException(
            status_code=401,
            detail={"message": "Срок действия токена истёк"},
        )
    user_id: str = payload.get("sub")
    if not user_id:
        raise ClientErrorApiException(
            status_code=401,
            detail={"message": "Нет id пользователя в токене"},
        )
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise ClientErrorApiException(
            status_code=401,
            detail={"message": "Пользователь с таким id не существует"},
        )
    return user
