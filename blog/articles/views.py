from flask import Blueprint, render_template

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
def articles_detail(id):
    article = Article.query.filter_by(id=id).one_or_none()
    if article is None:
        title = 'Статья не найдена'
        return render_template('articles/article_detail.html',
                               title=title)

    else:
        return render_template('articles/article_detail.html',
                               title=f'{article.title}',
                               article=article)

