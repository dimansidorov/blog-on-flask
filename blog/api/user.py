from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.users.models import User
from blog.schemas import UserSchema
from blog.database import db
from blog.permissions.users import UserPermission


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
        'model': User,
        "permission_get": [UserPermission],
    }
