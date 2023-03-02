import datetime

from blog.database import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'{self.title} by {self.creator_id}'
