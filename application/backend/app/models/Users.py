from pydantic import BaseModel


# тут надо будет добавить баланс ?
class UserSafe(BaseModel):
    login: str
