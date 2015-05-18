from flask.ext.wtf import Form
from flask.ext.uploads import *
from wtforms import TextField, RadioField, DateField, FileField, PasswordField
from wtforms.validators import DataRequired, Required, InputRequired
from wtforms import validators
from flask_wtf.file import FileField, FileAllowed, FileRequired


class Signup(Form):
  email = TextField('Email', validators=[InputRequired()])
  password = PasswordField('Password', validators=[InputRequired()])
  
class Profile(Form):
  fname = TextField('fname', validators=[InputRequired()])
  lname = TextField('lname', validators=[InputRequired()])
  username = TextField('username', validators=[InputRequired()])
  sex = RadioField('Sex', choices=[('Male','Male'), ('Female', 'Female')], validators=[InputRequired()])
  age = DateField('age', format='%Y-%m-%d', validators=[DataRequired()])
  image = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
                                         

  