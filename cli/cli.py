import click

from shared.trips import TripGenerator
from static.constants import NUM_OF_MONUMENTS


@click.command('generate-trip')
@click.option('-n', '--number', required=True, type=int)
def generate_trip(number: int):
    """ Generate trip."""
    if number > NUM_OF_MONUMENTS:
        raise ValueError(f"Max number of monuments ({NUM_OF_MONUMENTS}) exceeded.")
    trip = TripGenerator(number)
    trip.run()


if __name__ == "__main__":
    generate_trip()
