from flask import Blueprint, render_template, redirect, request, current_app, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from blog.database import db

from blog.articles.forms import CreateArticleForm
from blog.authors.models import Author
from blog.articles.models import Article

articles = Blueprint(
    'articles',
    __name__,
    url_prefix='/articles',
    static_folder='../static'
)


@articles.route('/', endpoint='list')
def articles_list():
    all_articles = Article.query.all()
    return render_template('articles/articles.html', title='Статьи', articles=all_articles)


@articles.route('/<id>', endpoint='detail')
@login_required
def articles_detail(id):
    article = Article.query.filter_by(id=id).one_or_none()
    if article is None:
        title = 'Статья не найдена'
        return render_template('articles/article_detail.html',
                               title=title)

    else:
        return render_template('articles/article_detail.html',
                               title=f'Статья о "{article.title}"',
                               article=article)


@articles.route('/add_article', methods=['GET', 'POST'], endpoint='add_article')
@login_required
def add_article():
    title = 'Добавить статью'
    error = None
    form = CreateArticleForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        if current_user.author:
            author_id = int(str(current_user.author)[1:-1])
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.commit()
            author_id = int(str(current_user.author)[1:-1])

        article = Article(title=form.title.data, body=form.body.data, author_id=author_id)
        db.session.add(article)

        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles.detail", id=article.id, title=article.title))

    return render_template('articles/add_article.html', form=form, title=title, errors=error)
