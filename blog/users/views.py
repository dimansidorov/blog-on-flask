from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users = Blueprint(
    'users',
    __name__,
    url_prefix='/users',
    template_folder='../templates',
    static_folder='../static'
)

MENU = {
    'Статьи': 'articles.articles_list',
    'Пользователи': 'users.users_list',
    # 'О сайте': '#'
}
USERS = {
    'varlamov': 'Илья Варламов',
    'urgantcom': 'Иван Ургант',
    'slavakomissarenko': 'Вячеслав Комиссаренко',
    'ana_d_armas': 'Ана де Армас'
}


@users.route('/')
def users_list():
    return render_template('users/users.html',
                           title='Пользователи',
                           menu=MENU,
                           users=USERS)


@users.route('/<slug>')
def user_detail(slug):
    try:
        user = USERS[slug]
        return render_template('users/user_detail.html',
                               title=f'информация о {user}',
                               user=user,
                               menu=MENU)
    except KeyError:
        title = 'Пользователь не найден'
        return render_template('users/user_detail.html',
                               title=title,
                               user=title,
                               menu=MENU)
