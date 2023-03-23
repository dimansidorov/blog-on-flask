from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.users.models import User
from blog.schemas import UserSchema
from blog.database import db


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User
    }