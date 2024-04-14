from os.path import abspath, dirname
from typing import Optional


def get_database_location(is_windows: Optional[bool] = None) -> str:
    """ Provides absolute value of the database directory. """
    ending = "/"
    if is_windows:
        ending = '\\'
    return abspath(dirname(dirname(__file__))) + ending + "static" + ending + "monumentsCracow.sqlite"
