from sqlalchemy import Column, Integer, String

from app.core.settings import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    login = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    confirm_code = Column(Integer, nullable=False)
