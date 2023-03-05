from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    first_name = StringField('Имя')
    last_name = StringField("Фамилия")
    username = StringField("Логин")
    email = StringField('Email',
                        [
                            validators.Email(),
                            validators.DataRequired(),
                            validators.Length(min=10, max=200)
                        ],
                        filters=[lambda x: x and x.lower()])


class RegisterUserForm(UserBaseForm):
    password = PasswordField(
        'Пароль',
        [
            validators.DataRequired(),
            validators.EqualTo('confirm', message='Пароли должны сопадать')
        ]
    )
    confirm = PasswordField('Повторите пароль')
    submit = SubmitField('Зарегистрироваться')


class LoginForm(FlaskForm):
    username = StringField("Логин", [validators.DataRequired()])
    password = PasswordField('Пароль', [validators.DataRequired()])
    submit = SubmitField('Войти')

