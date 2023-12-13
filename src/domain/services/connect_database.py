from domain.models.database_settings import DatabaseSettings
from domain.services.create_database_controller import CreateDatabaseController

class ConnectDatabase:
    def create_connection(self, database_settings: DatabaseSettings) -> CreateDatabaseController:
        raise NotImplementedError()