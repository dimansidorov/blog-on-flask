from flask import Flask
from blog.articles.views import articles
from blog.users.views import users


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(blueprint=articles, name='articles')
    app.register_blueprint(blueprint=users, name='users')
