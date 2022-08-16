import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

DATABASE_URL = "sqlite:////tmp/:memory:"
TEST_DATABASE_URL = "sqlite:////tmp/:memory:"

password = os.environ.get('DB_PASSWORD', None)

# if password has '@' in it, it's a secret key
if password is not None and '@' in password:
    password = password.replace('@', '%40')

if os.getenv('DATABASE') == 'mysql':
    DATABASE_URL = "mysql://{user}:{password}@{host}:{port}/{database}".format(
        user=os.getenv('DB_USER', 'root'),
        password=password,
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '3306'),
        database=os.getenv('DB_DATABASE'),
    )
elif os.getenv('DATABASE') == 'postgres':
    DATABASE_URL = "postgres://{user}:{password}@{host}:{port}/{database}".format(
        user=os.getenv('DB_USER', 'root'),
        password=password,
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432'),
        database=os.getenv('DB_DATABASE'),
    )
