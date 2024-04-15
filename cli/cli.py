import click

from shared.trips import TripGenerator


@click.command('generate-trip')
@click.option('-n', '--number', required=True, type=int)
def generate_trip(number: int):
    """ Generate trip."""
    # number = 4
    trip = TripGenerator(number)
    trip.run()


if __name__ == "__main__":
    generate_trip()
