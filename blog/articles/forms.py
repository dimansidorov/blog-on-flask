from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, SubmitField


class CreateArticleForm(FlaskForm):
    title = StringField(
        'Название статьи',
        [validators.DataRequired()]
    )
    body = TextAreaField(
        'Статья',
        [validators.DataRequired()]
    )
    submit = SubmitField('Добавить статью')
