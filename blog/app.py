from flask import Flask
from blog.articles.views import articles
from blog.auth.views import auth_app, login_manager
from blog.users.views import users
from blog.database import db
import os


def create_app() -> Flask:
    app = Flask(__name__)
    cfg_name = os.environ.get('DevConfig')
    app.config.from_object(f'blog.configs.DevConfig')
    db.init_app(app)
    register_blueprints(app)
    login_manager.init_app(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(blueprint=articles, name='articles')
    app.register_blueprint(blueprint=users, name='users')
    app.register_blueprint(blueprint=auth_app, name='auth_app')
