<p align="center">
<img src="https://banners.beyondco.de/Flask%20Boilerplate.png?theme=light&packageManager=Happy&packageName=Coding&pattern=charlieBrown&style=style_2&description=Production+ready+batteries+included+boilerplate.&md=1&showWatermark=1&fontSize=100px&images=adjustments&widths=50&heights=50">
</p>

### Flask Boilerplate

A production-grade flask application that you can start your projects without hesitation and without worrying about managing the project structure.


**Features**
- [x] Factory Pattern
- [x] SQLAlchemy ORM
- [x] Flask-Migrate for database migrations
- [x] Flask-Seeder for database seed
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
flask db upgrade

# rollback database migrations
flask db downgrade

# run database seeder, this will setup default admin credentials for our backend
python seed run
```

**Running Application**

You can run application using multiple methods:

```python
# using wsgi
python wsgi.py

# gunicorn server
gunicorn -w 4 wsgi:app -t 90 0.0.0.0:5000 --reload

# using sh
./run
```

**ORM**

This application uses orator orm. You can find details **[here](https://orator-orm.com/)**. Some basic commands:

```sh
# Creating migration
flask db migrate -m "migration_message_here"

# Run migration
flask db upgrade

# Rollback migration
flask db downgrade
```

**Celery**

For task queues and heavy background services, **[Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)** is used. **[Redis](https://redis.io/)** has been used as broker.

```sh
# Start celery worker

celery -A celery_worker.celery worker --pool=solo --loglevel=info
```

## Contributions

Contributions are welcome! If you have any questions or suggestions, please feel free to open an issue or create a pull request.