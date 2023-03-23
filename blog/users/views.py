from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

from blog.users.models import User

users = Blueprint(
    'users',
    __name__,
    url_prefix='/users',
    template_folder='../templates',
    static_folder='../static'
)


@users.route('/', endpoint='list')
@login_required
def user_list():
    if current_user.is_staff:
        all_users = User.query.all()
        return render_template('users/users.html',
                               title='Пользователи',
                               users=all_users)
    return redirect(url_for('articles.list'))


@users.route('/<id>', endpoint='detail')
@login_required
def user_detail(id):
    if current_user.is_staff:
        user = User.query.filter_by(id=id).one_or_none()
        if user is None:
            title = 'Пользователь не найден'
            return render_template('users/user_detail.html',
                                   title=title)

        else:
            return render_template('users/user_detail.html',
                                   title=f'Пользователь {user.username}',
                                   user=user)
    else:
        return redirect(url_for('articles.list'))
