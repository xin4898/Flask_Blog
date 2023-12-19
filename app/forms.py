from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('使用者名稱',validators=[DataRequired()])
    password = PasswordField('密碼',validators=[DataRequired()])
    remember_me = BooleanField('記住我')
    submit = SubmitField('登入')

class RegistrationForm(FlaskForm):
    username = StringField('使用者名稱', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('密碼', validators=[DataRequired()])
    password2 = PasswordField('再輸入一次密碼', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('註冊')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('該使用者名稱已存在')
        
    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('該 email 已存在')