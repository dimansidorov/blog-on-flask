from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.articles.models import Article
from blog.schemas import ArticleSchema
from blog.database import db


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article
    }
