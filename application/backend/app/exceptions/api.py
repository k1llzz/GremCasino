from fastapi import HTTPException


class ClientErrorApiException(HTTPException):
    """Исключение, вызываемое, когда происходит ошибка данных, введенных пользователем"""

    pass
