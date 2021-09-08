### Flask Boilerplate

**Running Application**

First of all copy `.env.example` and create new `.env` file. And then,

```python
# create virtual environment
python -m venv venv

# activate virtual environment
source venv/bin/activate

# install project dependencies
pip install -r requirements.txt

# start gunicorn server
gunicorn -w 4 wsgi:server -t 90 0.0.0.0:5000 --reload
```

**ORM**

This application uses orator orm. You can find details **[here](https://orator-orm.com/)**. Some basic commands:

```sh
# Creating migration
python db.py make:migration create_users_table

# Run migration
python db.py migrate

# Rollback migration
python db.py migrate:rollback

# For more details run:
python db.py
```

**Celery**

For task queues and heavy background services, **[Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)** is used. **[Redis](https://redis.io/)** has been used as broker.