### Flask Boilerplate

A production-grade flask application that you can start your projects without hesitation and without worrying about managing the project structure.


**Features**
- [x] Factory Pattern
- [x] Orator ORM module
- [x] Celery for background jobs
- [x] Managed Routing using Blueprints
- [x] Data and Route Caching using Flask-Cache
- [x] File Storage using Depot
- [x] Authentication using Flask-Login
- [x] Email using Flask-Mail

**Application Setup**

First of all copy `.env.example` and create new `.env` file. Set required configurations for mails and databases in `.env`.

```sh
# create virtual environment
python -m venv venv

# activate virtual environment
source venv/bin/activate

# install project dependencies
pip install -r requirements.txt

# migrate database
python db.py migrate

# run database seeder, this will setup default admin credentials for our backend
python db.py db:seed
```

**Running Application**

You can run application using multiple methods:

```python
# using wsgi
python wsgi.py

# gunicorn server
gunicorn -w 4 wsgi:server -t 90 0.0.0.0:5000 --reload

# using sh
./run
```

**ORM**

This application uses orator orm. You can find details **[here](https://orator-orm.com/)**. Some basic commands:

```sh
# Creating migration
python db.py make:migration create_users_table --create --table=users

# Run migration
python db.py migrate

# Rollback migration
python db.py migrate:rollback

# For more details run:
python db.py
```

**Celery**

For task queues and heavy background services, **[Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)** is used. **[Redis](https://redis.io/)** has been used as broker.

```sh
# Start celery worker

celery -A celery_worker.celery worker --pool=solo --loglevel=info
```