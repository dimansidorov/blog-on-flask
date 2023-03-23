from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.authors.models import Author
from blog.articles.models import Article
from blog.schemas import AuthorSchema
from blog.database import db

from combojsonapi.event.resource import EventsResource


class AuthorEventList(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return f'Cтатей у автора - {Article.query.filter(Article.author_id == kwargs["id"]).count()}'

class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author
    }


class AuthorDetail(ResourceDetail):
    events = AuthorEventList
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author
    }
