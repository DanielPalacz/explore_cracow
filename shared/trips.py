from typing import TypeVar

import click

from shared.funcs import get_database_location
from shared.sql_sqlite_client import SqliteClient
from static.constants import SQL_QUERY
from random import randint


DB_LOCATION = get_database_location()
""" Provides absolute value of the database directory. """

MonumentItemT = TypeVar("MonumentItemT", bound="MonumentItem")


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

    def __init__(self, n: int):
        self.__monuments = pick_n_random_monuments(n)

    def run(self) -> None:
        sorted_monuments = sorted(self.__prepare_trip_monuments())
        print("Start here:")
        print(" -", sorted_monuments[0])
        for monument in sorted_monuments[1:]:
            print("Later, go there:")
            print(" -", monument)
        else:
            print()
            print("Your trip just has finished.")

    def __prepare_trip_monuments(self) -> list[MonumentItemT]:
        monuments = []

        for random_monument in self.__monuments:
            monument_item = MonumentItem(
                name=random_monument[1],
                chronology=random_monument[2],
                city=random_monument[3],
                street=random_monument[4],
                street_number=random_monument[5],
                width_coordinate=random_monument[6],
                longitude=random_monument[7]
            )
            monuments.append(monument_item)
        return monuments


class MonumentItem:

    def __init__(
            self, name: str, chronology: str, city: str, street: str, street_number: str, width_coordinate, longitude):
        self.__name: str = name
        self.__chronology: str = chronology
        self.__city: str = city
        self.__street_address: str = street + " " + street_number
        self.__width_coordinate: float = float(width_coordinate)
        self.__longitude: float = float(longitude)

    def __str__(self):
        return f"{self.name}, [{self.__chronology}, {self.__city}, {self.__street_address}]"

    def __le__(self, other):
        geogr_location = self.__width_coordinate * self.__width_coordinate + self.__longitude * self.__longitude
        other_geogr_location = (
                other.__width_coordinate * other.__width_coordinate + other.__longitude * other.__longitude)
        return geogr_location <= other_geogr_location

    def __lt__(self, other):
        geogr_location = self.__width_coordinate * self.__width_coordinate + self.__longitude * self.__longitude
        other_geogr_location = (
                other.__width_coordinate * other.__width_coordinate + other.__longitude * other.__longitude)
        return geogr_location < other_geogr_location

    def __ge__(self, other):
        geogr_location = self.__width_coordinate * self.__width_coordinate + self.__longitude * self.__longitude
        other_geogr_location = (
                other.__width_coordinate * other.__width_coordinate + other.__longitude * other.__longitude)
        return geogr_location > other_geogr_location

    def __gt__(self, other):
        geogr_location = self.__width_coordinate * self.__width_coordinate + self.__longitude * self.__longitude
        other_geogr_location = (
                other.__width_coordinate * other.__width_coordinate + other.__longitude * other.__longitude)
        return geogr_location > other_geogr_location

    @property
    def name(self) -> str:
        """ Provides monument name. """
        return self.__name
