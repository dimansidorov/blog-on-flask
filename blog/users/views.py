from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

from blog.users.models import User

users = Blueprint(
    'users',
    __name__,
    url_prefix='/users',
    template_folder='../templates',
    static_folder='../static'
)


@users.route('/', endpoint='list')
def users_list():
    if current_user.is_authenticated:
        all_users = User.query.all()
        return render_template('users/users.html',
                               title='Пользователи',
                               users=all_users)
    return redirect(url_for('auth_app.login'))




@users.route('/<slug>', endpoint='detail')
def user_detail(slug):
    if current_user.is_authenticated:
        user = User.query.filter_by(username=slug).one_or_none()
        if user is None:
            title = 'Пользователь не найден'
            return render_template('users/user_detail.html',
                                   title=title)

        else:
            return render_template('users/user_detail.html',
                                   title=f'{user.username}',
                                   user=user)
    else:
        return redirect(url_for('auth_app.login'))
