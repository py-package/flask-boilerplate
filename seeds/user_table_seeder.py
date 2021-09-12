from orator.seeds import Seeder
from werkzeug.security import generate_password_hash
from datetime import datetime


class UserTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('users').insert({
            'name': 'admin',
            'email': 'admin@example.com',
            'password': generate_password_hash('admin'),
            'email_verified_at': datetime.now(),
        })
