import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://blog_database_7mag_user:xG4oRTjPO1T2DbRWvH4weEOhTrfJTOjz@dpg-cghh73fdvk4ml9ulrogg-a.frankfurt-postgres.render.com/blog_database_7mag'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '3a+*q6&rjy0#6^57w#6j&+j0lol_$nh*=4$^d*(@2m%r@lnis%'
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cerulean'

    OPENAPI_URL_PREFIX = '/api/swagger'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '4.18.1'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True
