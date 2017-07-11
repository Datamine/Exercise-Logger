from os import environ

from flask_login import current_user, login_required, login_user, logout_user
from flask import Flask, render_template, redirect, flash, jsonify
from flask_bootstrap import Bootstrap

from auth import login_manager
from forms import LoginForm, RegistrationForm
from models import User, Swimming
from db_connect import session


app = Flask(__name__)
app.config['SECRET_KEY'] = environ['CSRF_TOKEN']
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager.init_app(app)
Bootstrap(app)


@app.route('/api/request_logs')
@login_required
def request_logs():

    exercise_types = [
        Swimming,
    ]

    days_to_exercises_map = {}

    for e in exercise_types:
        exercise_rows = session.query(e).filter(e.user_id==current_user.id).all()
        for exercise_row in exercise_rows:
            exercise_date = exercise_row.exercise_date
            if exercise_date in days_to_exercises_map:
                days_to_exercises_map[exercise_date].append(exercise_row.renderable_dict)
            else:
                days_to_exercises_map[exercise_date] = [exercise_row.renderable_dict]

    return jsonify(days_to_exercises_map)


@app.route('/view_logs')
@login_required
def view_logs():
    return render_template(
        'view_logs.html',
        title='View Logs',
        name='view_logs',
        scripts=[
            '/js/view_logs.js',
        ]
    )



@app.route('/enter_data')
@login_required
def enter_data():
    return 'foo'


@app.route('/settings')
@login_required
def settings():
    # let them decide between metric and imperial
    # let them set their exercises to appear on the log_data page
    # let them export data
    # let them delete account
    # let them set new password/email
    return 'foo'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            password=form.password.data,
        )
        session.add(user)
        session.commit()
        flash('You can now log in.')
        return redirect('/login')

    return render_template(
        'login_or_register.html',
        title='Register',
        name='register',
        form=form
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = session.query(User).filter(User.email == form.email.data).first()
        if (not user is None) and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect('/')
        else:
            flash('Invalid username or password.')

    return render_template(
        'login_or_register.html',
        title='Login',
        name='login',
        form=form,
    )


@login_required
@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect('/login')


@app.route('/')
def index():
    return redirect('/enter_data')


if __name__ == '__main__':
    app.run(debug=True)
