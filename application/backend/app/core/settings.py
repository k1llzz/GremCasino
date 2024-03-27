from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/gremcasino"
)

Base = declarative_base()

MAIL = "gremkazino@mail.ru"
MAIL_PASSWORD = "19bx2r2ekmBZHGz47TPu"
