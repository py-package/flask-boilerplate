import os

from config.database import database
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)


class Config(object):
    DEBUG = False
    KEY = os.getenv('APP_KEY')


# Create the development config
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL')
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
