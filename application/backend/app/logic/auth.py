from app.core.settings import async_session_maker
from app.db.repos.DAO import BaseDAO
from app.db.tables.users import Users
from app.exceptions.api import ClientErrorApiException
from sqlalchemy import select

# моделька пайдентик
# from app.models.Users import UserSafe


class UsersDAO(BaseDAO):
    model = Users

    # эта функция должна возвращать данные о пользователе, которые будут на главной странице, по факту только логин и
    # баланс(когда добавишь его в табличку) + ты говорил, что надо возвращать данные в виде Model(**otvev_bd.dict()),
    # но у меня чот не пошло
    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()


def check_email(string):
    if " " in string:
        return False
    if "@" not in string:
        return False
    name, domain = string.split("@", 1)
    if "." not in domain[1:]:
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
