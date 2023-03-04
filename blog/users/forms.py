from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    first_name = StringField('Имя')
    last_name = StringField("Фамилия")
    username = StringField("Имя пользователя")
    email = StringField('Email',
                        [
                            validators.Email(),
                            validators.DataRequired(),
                            validators.Length(min=10, max=200)
                        ],
                        filters=lambda x: x and x.lower())


class RegisterUserForm(UserBaseForm):
    password = PasswordField(
        'Пароль',
        [
            validators.DataRequired(),
            validators.EqualTo('confirm', message='Пароли должны сопадать')
        ]
    )
    confirm = PasswordField('Повтор пароля')
    submit = SubmitField('Зарегистрироваться')
