# -*- coding: utf-8 -*-
"""This module implements client wrapper for sqlite database.

Attributes:
    SqliteConn (TypeVar): custom typing type bound to 'sqlite3.Connection'
"""


import sqlite3
from typing import Optional, TypeVar

from shared.funcs import get_database_location
from static.constants import SQL_QUERY

SqliteConn = TypeVar("SqliteConn", bound="sqlite3.Connection")


class SqliteClient:
    """ Sqlite client wrapper.

    Args:
        location (str, None): Path to database file. None means in-memory database.
        **connection_params: Arbitrary keyword arguments used for connection setup.

    Attributes:
        __connection (SqliteConn, None): Sqlite connection object.
        __location (str, None): Path to database file. ':memory:' means in-memory database.
        __connection_params (dict): Arbitrary keyword arguments used for connection setup.
    """

    def __init__(self, location: Optional[str] = None, **connection_params):
        self.__location = location or ":memory:"
        self.__connection: Optional[SqliteConn] = None
        self.__connection_params: dict = connection_params

    def __enter__(self):
        self.__setup_connection()
        return self

    def __exit__(self, *args, **kwargs):
        self.__close_connection()

    @property
    def connection(self) -> SqliteConn:
        """SqliteConn: Sqlite connection object."""
        if self.__connection is None:
            self.__setup_connection()
        return self.__connection

    def insert(self, **kwargs) -> None:
        pass

    def select(self, sql_query) -> list[tuple]:
        return self.__connection.execute(sql_query).fetchall()

    def __setup_connection(self) -> None:
        connection = sqlite3.connect(
            self.__location,
            detect_types=sqlite3.PARSE_DECLTYPES,
            **self.__connection_params
        )
        self.__connection = connection

    def __close_connection(self, **kwargs) -> None:
        self.__connection.close()


if __name__ == "__main__":
    db_location = get_database_location()
    print(db_location)
    with SqliteClient(db_location) as sqlite_client:
        records = sqlite_client.select(SQL_QUERY)
        for row in records:
            print(row)
