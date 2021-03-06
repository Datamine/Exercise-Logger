from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
import datetime

from .base import Base

def serialize_datetime(d: datetime) -> str:
    return d.strftime("%Y-%m-%d %H:%M")

class Exercise():
    @property
    def exercise_date(self):
        return self.created_at.strftime("%Y-%m-%d")

    @property
    def exercise_time(self):
        return self.created_at.strftime("%H:%M")

    @property
    def exercise_name(self):
        return self.__tablename__.capitalize()

class Swimming(Base, Exercise):
    __tablename__ = 'swimming'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    # number of lanes
    lanes = Column(Integer)
    # length per lane in the user's units
    length = Column(Integer)
    # time taken as hours:minutes
    hours = Column(Integer)
    minutes = Column(Float)

    @property
    def renderable_dict(self):
        return {
            "created_date": self.exercise_date,
            "created_time": self.exercise_time,
            "exercise_name": self.exercise_name,
            "lanes": self.lanes,
            "length": self.length,
            "hours": self.hours,
            "minutes": self.minutes,
        }
