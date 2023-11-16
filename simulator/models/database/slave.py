import logging

from models.database import Database

LOGGER = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
LOGGER.addHandler(stream_handler)
LOGGER.setLevel(logging.DEBUG)


class Slave(Database):
    def __init__(
            self,
            host: str = 'localhost',
            user: str = 'root',
            password: str = '1234567',
            database: str = 'slave',
    ) -> None:
        super().__init__(host, user, password, database)
