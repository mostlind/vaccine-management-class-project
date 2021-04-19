import uuid
import click
from click.termui import prompt
from click.utils import echo
from entities.facility import FacilityManager, Facility


@click.group()
def facility():
    pass


@click.command()
def register():
    name = prompt("What is the facility name?\nEnter Name: ")
    address = prompt("\nWhat is the address of the facility?\nEnter Address: ")
    number_of_vaccines = prompt(
        "\nHow many vaccines do you have?\nEnter Number: ", type=int
    )

    facility_manager = FacilityManager()
    facility = Facility(
        name=name, address=address, number_of_vaccines=number_of_vaccines
    )

    facility_manager.save(facility)

    echo(f"\nRegistered Facility with id {facility.id}")


@click.command()
@click.option("--id", help="The unique identifier for the facility")
def lookup(id: str):
    facility_manager = FacilityManager()
    facility = facility_manager.find_by_id(uuid.UUID(id))

    if facility is None:
        echo(f"Could not find a facility with id {id}")
        return
    echo("Found Facility")
    echo("----------------------------------")
    echo(f"Name: {facility.name}")
    echo(f"Address: {facility.address}")
    echo(f"Number of Vaccines: {facility.number_of_vaccines}")


@click.command()
def list():
    facility_manager = FacilityManager()
    facilities = facility_manager.all()
    echo("Id,Name")
    for facility in facilities:
        echo(f"{facility.id},{facility.name}")


facility.add_command(register)
facility.add_command(lookup)
facility.add_command(list)