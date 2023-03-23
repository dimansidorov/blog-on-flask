from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.articles.models import Article
from blog.schemas import ArticleSchema
from blog.database import db

from combojsonapi.event.resource import EventsResource


class ArticleEventList(EventsResource):
    def event_get_count(self):
        return f'Всего статей: {Article.query.count()}'


class ArticleList(ResourceList):
    events = ArticleEventList
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
