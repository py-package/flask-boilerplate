from seeds.user_table_seeder import UserTableSeeder
from orator.seeds import Seeder


class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(UserTableSeeder)
