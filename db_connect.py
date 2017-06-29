from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ

try:
    path = "postgresql://" + environ['DATABASE_URL']
    engine = create_engine(path)

    session = scoped_session(sessionmaker(bind=engine))
except KeyError:
    pass
