from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, SubmitField, SelectMultipleField, FileField
from flask_wtf.file import FileField, FileAllowed


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
    cover = FileField('Обложка')
    submit = SubmitField('Добавить статью')


class UpdateArticleForm(FlaskForm):
    title = StringField(
        'Новое название статьи'
    )
    body = TextAreaField(
        'Обновленный текст статьи'
    )
    cover = FileField('Новая обложка')
    submit = SubmitField('Обновить статью')