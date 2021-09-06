import os
from config.database import database

basedir = os.path.abspath(os.path.dirname(__name__))


class Config(object):
    DEBUG = False
    KEY = os.environ.get('APP_KEY')


# Create the development config
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    ORATOR_DATABASES = database


# Create the testing config
class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    ORATOR_DATABASES = database

# create the production config


class ProductionConfig(Config):
    DEBUG = False
    ORATOR_DATABASES = database
