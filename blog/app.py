from flask import Flask
from blog.articles.views import articles
from blog.auth.views import auth_app, login_manager
from blog.users.views import users
from blog.database import db
from blog.security import flask_bcrypt
import os

from flask_migrate import Migrate


def create_app() -> Flask:
    app = Flask(__name__)
    cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
    app.config.from_object(f'blog.configs.{cfg_name}')
    flask_bcrypt.init_app(app)
    db.init_app(app)
    register_blueprints(app)
    login_manager.init_app(app)

    migrate = Migrate(app, db, compare_type=True)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(blueprint=articles, name='articles')
    app.register_blueprint(blueprint=users, name='users')
    app.register_blueprint(blueprint=auth_app, name='auth_app')
