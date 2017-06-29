from flask_login import LoginManager

from models import User
from db_connect import session


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))
