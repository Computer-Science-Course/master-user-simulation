import logging

import mysql.connector

LOGGER = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
LOGGER.addHandler(stream_handler)
LOGGER.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '[%(asctime)s] - [%(name)s] - [%(levelname)s] %(message)s'
)
stream_handler.setFormatter(formatter)


class Database:
    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        database: str,
    ) -> None:
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self._connection = None
        self._cursor = None
        LOGGER.info('%s instance initialized' % self.__class__.__name__)

    def connect(self) -> None:
        self._connection = mysql.connector.connect(
            host=self._host,
            user=self._user,
            password=self._password,
            database=self._database,
        )
        self._cursor = self._connection.cursor()
        LOGGER.info('%s instance connected' % self.__class__.__name__)

    def disconnect(self) -> None:
        self._cursor.close()
        self._connection.close()
        LOGGER.info('%s instance disconnected' % self.__class__.__name__)

    def get_users(self) -> list:
        self.connect()
        self._cursor.execute('SELECT * FROM users')
        users = self._cursor.fetchall()
        self.disconnect()
        return users

    def get_user(self, user_id: int) -> tuple:
        self.connect()
        self._cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user = self._cursor.fetchone()
        self.disconnect()
        return user

    def create_user(
            self,
            name: str,
            username: str,
            password: str,
    ) -> None:
        self.connect()
        self._cursor.execute(
            'INSERT INTO users (name, username, password) VALUES (%s, %s, %s)',
            (name, username, password),
        )
        self._connection.commit()
        self.disconnect()

    def update_user(
            self,
            user_id: int,
            name: str,
            username: str,
            password: str,
    ) -> None:
        self.connect()
        self._cursor.execute(
            'UPDATE users SET name = %s, username = %s, password = %s WHERE id = %s',
            (name, username, password, user_id),
        )
        self._connection.commit()
        self.disconnect()

    def delete_user(self, user_id: int) -> None:
        self.connect()
        self._cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
        self._connection.commit()
        self.disconnect()
