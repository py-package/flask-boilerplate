
from depot.manager import DepotManager


class Storage():

    @staticmethod
    def store(file):
        """
        Store a file in the storage.
        """
        depot = DepotManager.get()
        return depot.create(file)

    @staticmethod
    def get(key):
        """
        Get a file from the storage.
        """
        depot = DepotManager.get()
        return depot.get(key)

    def delete(key):
        """
        Delete a file from the storage.
        """
        depot = DepotManager.get()
        return depot.delete(key)
