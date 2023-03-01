

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '3a+*q6&rjy0#6^57w#6j&+j0lol_$nh*=4$^d*(@2m%r@lnis%'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'


class TestingConfig(BaseConfig):
    TESTING = True
