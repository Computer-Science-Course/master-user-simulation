import logging

from models.database import Database
from models.database.slave import Slave

LOGGER = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
LOGGER.addHandler(stream_handler)
LOGGER.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '[%(asctime)s] - [%(name)s] - [%(levelname)s] %(message)s'
)
stream_handler.setFormatter(formatter)


class Master(Database):
    def __init__(
            self,
            host: str = 'localhost',
            user: str = 'root',
            password: str = '1234567',
            database: str = 'master',
    ) -> None:
        super().__init__(host, user, password, database)
        self._slave = Slave()

    def create_user(
            self,
            name: str,
            username: str,
            password: str,
    ) -> None:
        try:
            self.connect()
            self._cursor.execute(
                'INSERT INTO users (name, username, password) VALUES (%s, %s, %s)',
                (name, username, password)
            )
            self._connection.commit()
            LOGGER.info('User created on master')
            self._slave.create_user(name, username, password)
            LOGGER.info('User replicated on slave')
        except Exception as e:
            self._slave.create_user(name, username, password)
            LOGGER.info('User created on slave')
            try:
                self.disconnect()
            except Exception as e:
                pass

    def get_users(self) -> list:
        try:
            self.connect()
            self._cursor.execute('SELECT * FROM users')
            users = self._cursor.fetchall()
            LOGGER.info('Users fetched from master')
            self.disconnect()
            return users
        except Exception as e:
            try:
                self.disconnect()
            except Exception as e:
                pass
            users = self._slave.get_users()
            LOGGER.info('Users fetched from slave')
            return users

    def get_user(self, user_id: int) -> tuple:
        try:
            self.connect()
            self._cursor.execute(
                'SELECT * FROM users WHERE id = %s', (user_id,))
            user = self._cursor.fetchone()
            LOGGER.info('User fetched from master')
            self.disconnect()
            return user
        except Exception as e:
            try:
                self.disconnect()
            except Exception as e:
                pass
            user = self._slave.get_user(user_id)
            LOGGER.info('User fetched from slave')
            return user

    def update_user(
            self,
            user_id: int,
            name: str,
            username: str,
            password: str,
    ) -> None:
        try:
            self.connect()
            self._cursor.execute(
                'UPDATE users SET name = %s, username = %s, password = %s WHERE id = %s',
                (name, username, password, user_id),
            )
            self._connection.commit()
            LOGGER.info('User updated on master')
            self._slave.update_user(user_id, name, username, password)
            LOGGER.info('User replicated on slave')
        except Exception as e:
            self._slave.update_user(user_id, name, username, password)
            LOGGER.info('User updated on slave')
            try:
                self.disconnect()
            except Exception as e:
                pass

    def delete_user(self, user_id: int) -> None:
        try:
            self.connect()
            self._cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
            self._connection.commit()
            LOGGER.info('User deleted on master')
            self._slave.delete_user(user_id)
            LOGGER.info('User replicated on slave')
        except Exception as e:
            self._slave.delete_user(user_id)
            LOGGER.info('User deleted on slave')
            try:
                self.disconnect()
            except Exception as e:
                pass
