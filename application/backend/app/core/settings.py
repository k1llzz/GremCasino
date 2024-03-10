from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/gremcasino')

Base = declarative_base()
