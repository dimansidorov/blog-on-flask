from flask import Blueprint, render_template
from blog.models.user import User

users = Blueprint(
    'users',
    __name__,
    url_prefix='/users',
    template_folder='../templates',
    static_folder='../static'
)

MENU = {
    'Статьи': 'articles.list',
    'Пользователи': 'users.list',
    # 'О сайте': '#'
}


# USERS = {
#     'varlamov': 'Илья Варламов',
#     'urgantcom': 'Иван Ургант',
#     'slavakomissarenko': 'Вячеслав Комиссаренко',
#     'ana_d_armas': 'Ана де Армас'
# }


@users.route('/', endpoint='list')
def users_list():
    all_users = User.query.all()
    print(all_users)
    return render_template('users/users.html',
                           title='Пользователи',
                           menu=MENU,
                           users=all_users)


@users.route('/<slug>', endpoint='detail')
def user_detail(slug):
    user = User.query.filter_by(username=slug).one_or_none()
    if user is None:
        title = 'Пользователь не найден'
        return render_template('users/user_detail.html',
                               title=title,
                               menu=MENU)

    else:
        return render_template('users/user_detail.html',
                               title=f'{user.username}',
                               user=user,
                               menu=MENU)
