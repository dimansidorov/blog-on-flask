from flask import Blueprint, render_template

articles = Blueprint(
    'articles',
    __name__,
    url_prefix='/articles',
    static_folder='../static'
)

MENU = {
    'Статьи': 'articles.articles_list',
    'Пользователи': 'users.users_list',
    # 'О сайте': '#'
}


@articles.route('/')
def articles_list():
    return render_template('articles/articles.html', title='Статьи', menu=MENU)
