from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, SubmitField, SelectMultipleField, FileField


class CreateArticleForm(FlaskForm):
    title = StringField(
        'Название статьи',
        [validators.DataRequired()]
    )
    body = TextAreaField(
        'Статья',
        [validators.DataRequired()]
    )
    tags = SelectMultipleField('Теги', coerce=int)
    submit = SubmitField('Добавить статью')
