from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.authors.models import Author
from blog.schemas import AuthorSchema
from blog.database import db


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author
    }
