from marshmallow_jsonapi import Schema, fields
from combojsonapi.utils import Relationship


class ArticleSchema(Schema):
    class Meta:
        type_ = 'article'
        self_url = 'article_detail'
        self_url_kwargs = {'id': '<id>'}
        self_url_many = "article_list"

    id = fields.Integer(as_string=True)
    title = fields.String(allow_none=False)
    body = fields.String(allow_none=False)
    create_at = fields.DateTime(allow_none=False)
    update_at = fields.DateTime(allow_none=False)
    cover = fields.String(allow_none=False)

    author = Relationship(
        nested='AuthorSchema',
        attribute="author",
        related_url="author_detail",
        related_url_kwargs={"id": "<id>"},
        schema="AuthorSchema",
        type_="author",
        many=False,
    )

    tag = Relationship(
        nested='TagSchema',
        attribute="tag",
        related_url='tag_detail',
        related_url_kwargs={'id': '<id>'},
        schema='TagSchema',
        type_='author',
        many=True
    )

