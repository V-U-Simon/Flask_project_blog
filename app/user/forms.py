from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField, SubmitField
from wtforms import validators


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[validators.DataRequired(), validators.Length(min=4, max=25)],
    )
    email = EmailField(
        "Email Address",
        validators=[
            validators.DataRequired(),
            validators.Email(),
            validators.Length(min=6, max=35),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            validators.DataRequired(message=""),
            validators.Length(min=6, max=35),
            validators.EqualTo("password_confirm", message="Passwords must match"),
        ],
    )
    password_confirm = PasswordField(
        "Password confirm",
        validators=[
            validators.Length(min=6, max=35),
        ],
    )
    accept_rules = BooleanField(
        "I accept the site rules",
        [validators.InputRequired(message="Agree to terms and conditions")],
    )
    submit = SubmitField("Sign In")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
