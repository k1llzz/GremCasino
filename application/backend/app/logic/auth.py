from sqlalchemy.orm import Session

from app.core.settings import engine
from app.db.tables.users import Users
from app.exceptions.api import ClientErrorApiException
from app.logic.utils import generate_code_message


async def add_user(login: str, email: str, password: str):
    if "@" not in email or len(password) < 3:
        raise ClientErrorApiException(
            status_code=422,
            detail={"message": "Неверный email или пароль слишком короткий"},
        )
    code = await generate_code_message(email)
    with Session(autoflush=False, bind=engine) as session:
        if (
            session.query(Users).filter_by(email=email).first()
            or session.query(Users).filter_by(login=login).first()
        ):
            raise ClientErrorApiException(
                status_code=422,
                detail={
                    "message": "Пользователь с таким email или логином уже существует"
                },
            )
        user = Users(login=login, email=email, password=password, confirm_code=code)
        session.add(user)
        session.commit()


async def check_code(code: int, login: str):
    with Session(autoflush=False, bind=engine) as session:
        user = session.query(Users).filter_by(login=login).first()
        right_code = user.confirm_code
    if code != right_code:
        user.delete()
        session.commit()
        raise ClientErrorApiException(
            status_code=422,
            detail={"message": "Неверный код подтверждения"},
        )
    return True
