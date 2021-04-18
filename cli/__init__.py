import click
from cli.facility import facility
from cli.appointment import appointment


@click.group()
def cli():
    pass


cli.add_command(facility)
cli.add_command(appointment)