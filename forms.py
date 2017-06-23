from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])

    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('password2', message='Passwords must match.')
    ])

    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')
