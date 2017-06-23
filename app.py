from os import environ
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from auth import login_manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
app.config['SECRET_KEY'] = environ['CSRF_KEY']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ex_type = db.Column(db.String, nullable=False)

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect
    pass
    # TODO: gotta figure out the workflow here -- direct the user to one of 3 pages:
    # login/register, log_exercise, view_logs


if __name__ == '__main__':
    app.run(debug=True)
