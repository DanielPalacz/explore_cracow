from shared.funcs import get_database_location
from shared.sql_sqlite_client import SqliteClient
from static.constants import SQL_QUERY
from random import randint


DB_LOCATION = get_database_location()
""" Provides absolute value of the database directory. """


def get_monuments() -> list[tuple]:
    """ Provides list of tuples containing monuments.

    Returns:
        list of tuples containing monuments,
        example - tuple elements are grouped as below:
             (id, nazwa, chronologia, miejscowosc, ulica, nr_adresowy, szerokosc_geogr, dlugosc_geogr)
            [(5, 'willa', '1913 r.', 'Kraków', 'św. Bronisławy', '15', '50.05347769999999', '19.910736'), ...]
    """
    with SqliteClient(DB_LOCATION) as sqlite_client:
        rows = sqlite_client.select(SQL_QUERY)
        return rows


def get_one_random_monument(monuments: list[tuple]) -> tuple:
    """ Provides one random monument from the list of monuments

    Returns:
        example:
        (5, 'willa', '1913 r.', 'Kraków', 'św. Bronisławy', '15', '50.05347769999999', '19.910736')

    """
    num_of_monuments = len(monuments)
    random_integer = randint(1, num_of_monuments) - 1
    return monuments[random_integer]


def pick_n_random_monuments(n: int) -> list[tuple]:
    """ Provides one random monument from the list of monuments

    Return:
        list of tuples containing monuments.
    """
    monuments = get_monuments()
    random_monuments = []
    while len(random_monuments) < n:
        random_monument = get_one_random_monument(monuments)
        if random_monument not in random_monuments:
            random_monuments.append(random_monument)

    return random_monuments


class TripGenerator:

    def __init__(self, random_monuments):
        self.__monuments = random_monuments


if __name__ == "__main__":
    breakpoint()
    # location = get_database_location()
    # print(location)
    # with SqliteClient(location) as sqlite_client:
    #    records = sqlite_client.select(SQL_QUERY)
    #    breakpoint()
    #    for row in records:
    #        print(row)
