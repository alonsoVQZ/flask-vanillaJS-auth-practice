from flask_wtf import FlaskForm
from flask_wtf.csrf import ValidationError
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Length

from models import db, User

# Login Form
class LoginForm(FlaskForm):
  username = StringField('username', validators=[DataRequired(), Length(min=4)])
  email = EmailField('email', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
#Register Form
class RegisterForm(FlaskForm):
  username = StringField('username', validators=[DataRequired(), Length(min=4)])
  email = EmailField('email', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
  def validate_username(self):
    if db.session.execute(db.select(User).where(User.username == self.username.data)).scalar_one_or_none:
      raise ValidationError('Username already exists')
  def validate_email(self):
    if db.session.execute(db.select(User).where(User.email == self.email.data)).scalar_one_or_none:
      raise ValidationError('Email already exists.')
