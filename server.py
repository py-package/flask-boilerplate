from flask_orator import Orator
from app import factory

server = factory()
db = Orator(server)
