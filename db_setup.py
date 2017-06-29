from db_connect import session, engine
from models import Base

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
