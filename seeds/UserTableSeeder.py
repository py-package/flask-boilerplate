from flask_seeder import Seeder, Faker, generator
from werkzeug.security import generate_password_hash
from datetime import datetime
from app.models.User import User


class UserTableSeeder(Seeder):

    def run(self):
        self.db.session.add(User(
            name='admin',
            email='admin@example.com',
            password=generate_password_hash('admin'),
            email_verified_at=datetime.now(),
        ))
