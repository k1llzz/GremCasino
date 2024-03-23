from app.db.tables.users import Users
from app.exceptions.api import ClientErrorApiException
from app.logic.DAO import BaseDAO


class UsersDAO(BaseDAO):
    model = Users


def check_email(string):
    if ' ' in string:
        return False
    if "@" not in string:
        return False
    name, domain = string.split('@', 1)
    if '.' not in domain[1:]:
        return False
    return True


async def add_user(login: str, email: str, password: str):
    if not check_email(email):
        raise ClientErrorApiException(
            status_code=422,
            detail={"message": "Некорректный email"},
        )
    email = email.lower()
    existing_email = await UsersDAO.find_one_or_none(email=email)
    existing_login = await UsersDAO.find_one_or_none(login=login)
    if existing_email:
        raise ClientErrorApiException(
            status_code=422,
            detail={"message": "Пользователь с таким email уже существует"},
        )
    elif existing_login:
        raise ClientErrorApiException(
            status_code=422,
            detail={"message": "Пользователь с таким логином уже существует"},
        )
    else:
        if len(password) < 5:
            raise ClientErrorApiException(
                status_code=422,
                detail={"message": "Слишком короткий пароль"},
            )
        else:
            await UsersDAO.add(email=email, login=login, password=password)


async def login_user(emalog: str, password: str):
    if "@" in emalog:
        emalog = emalog.lower()
        user = await UsersDAO.find_one_or_none(email=emalog)
    else:
        user = await UsersDAO.find_one_or_none(login=emalog)
    if not user or not (password == user.password):
        raise ClientErrorApiException(
            status_code=404,
            detail={"message": "Введён некорректный логин и/или пароль"},
        )
    return user
