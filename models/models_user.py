from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

from .base import Base

class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    email = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


