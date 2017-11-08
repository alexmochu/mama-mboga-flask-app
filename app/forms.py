from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, length, Email, EqualTo, ValidationError

def validate_names(form, field):
    if field.data.isdigit():
        raise ValidationError(u"Must Contain Letters")

class SignUpForm(Form):
    username = StringField("Username", validators=[DataRequired(), length(min=4), validate_names ])
    email = StringField("Email", validators= [ DataRequired(), Email(message="Invalid Email Address"), length(min=4), validate_names])
    password = PasswordField('New Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords must match'), length(min=4, max=80)])
    confirm = PasswordField("Confirm Password")