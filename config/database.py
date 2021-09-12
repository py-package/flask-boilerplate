import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

database = {
    'default': os.getenv('DATABASE'),

    'mysql': {
        'driver': 'mysql',
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_DATABASE'),
    },

    'postgres': {
        'driver': 'postgres',
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_DATABASE'),
    },
}

test_database = {
    'default': 'sqlite',

    'sqlite': {
        'driver': 'sqlite',
        'database': ':memory:',
    },
}
