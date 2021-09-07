#from app import create_app, celery
from app import factory, celery

app = factory()
app.app_context().push()
