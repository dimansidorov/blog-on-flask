import datetime

from sqlalchemy import func

from blog.database import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow(), server_default=func.now())
    update_at = db.Column(db.DateTime, default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow())

    author = db.relationship('Author', back_populates='article')

    def __repr__(self):
        return f'{self.title} by {self.creator_id}'
