from flask import Flask
from blog.articles.views import articles
from blog.users.views import users
from blog.models.database import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = '3a+*q6&rjy0#6^57w#6j&+j0lol_$nh*=4$^d*(@2m%r@lnis%'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(blueprint=articles, name='articles')
    app.register_blueprint(blueprint=users, name='users')
