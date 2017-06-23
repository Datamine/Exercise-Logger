from flask import render_template, redirect, flash
from flask_login import LoginManager, login_user, logout_user, login_required

from forms import LoginForm, RegistrationForm

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))


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


def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = session.query(User).filter(User.email == form.email.data).first()
        if (not user is None) and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            # there are probably more useful/granular redirects I can use here
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
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect('/')
