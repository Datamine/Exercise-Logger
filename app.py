from os import environ

from flask_login import current_user, login_required
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap

from auth import login_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = environ['CSRF_TOKEN']
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager.init_app(app)

Bootstrap(app)

@login_required
@app.route('/enter_data')

@login_required
@app.route('/view_logs')
def view_logs

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect
    pass
    # TODO: gotta figure out the workflow here -- direct the user to one of 3 pages:
    # login/register, log_exercise, view_logs


if __name__ == '__main__':
    app.run(debug=True)
