from entities.facility import FacilityManager
from click.termui import prompt
from cli.facility import facility
from datetime import date, datetime, timedelta
import uuid
import click
from click.utils import echo
from entities.user import User, UserManager
from entities.appointment import Appointment, ApppointmentManager

# from facility import FacilityManager, Facility


@click.group()
def appointment():
    pass


@click.command()
def schedule():
    name = prompt("What your name?\nEnter Name: ")
    address = prompt("\nWhat is your address?\nEnter Address: ")
    date_of_birth = prompt("\nWhat is your date of birth in the format yyyy-mm-dd?")
    number_of_preexisting_conditions = prompt(
        "\nHow many pre-existing conditions do you have?\nEnter Number: ", type=int
    )

    parsed = datetime.strptime(date_of_birth, "%Y-%m-%d")

    user_manager = UserManager()
    user = User(
        name=name,
        address=address,
        date_of_birth=parsed,
        number_of_preexisting_conditions=number_of_preexisting_conditions,
    )

    user_manager.save(user)

    echo(f"\nRegistered User with id {user.id}")

    facility_id = prompt(
        "What is the unique identifier of the facility that you want to go to?"
    )

    appointment_date = date.today() + timedelta(days=3)

    appointment = Appointment(
        facility_id=uuid.UUID(facility_id), user_id=user.id, date=appointment_date
    )

    appointment_manager = ApppointmentManager()
    appointment_manager.save(appointment)

    echo(
        f"Appoinment scheduled on {appointment_date.isoformat()} with appointment id {appointment.id}"
    )


@click.command()
def list():
    appointment_manager = ApppointmentManager()
    appoinments = appointment_manager.all()

    echo("Id,Date,User Id,Facility Id")
    for appoinment in appoinments:
        echo(
            f"{appoinment.id},{appoinment.date},{appoinment.user_id},{appoinment.facility_id}"
        )


@click.command()
@click.option("--id", help="The unique identifier for the facility")
def lookup(id: str):
    appointment_manager = ApppointmentManager()
    facility_manager = FacilityManager()
    user_manager = UserManager()

    appointment = appointment_manager.find_by_id(uuid.UUID(id))
    user = user_manager.find_by_id(appointment.user_id)
    facility = facility_manager.find_by_id(appointment.facility_id)

    print(
        f"""Found Appointment
----------------------------------
Id: {str(appointment.id)}
User: {user.name}
Facility: {facility.name}
Date: {appointment.date}"""
    )


appointment.add_command(list)
appointment.add_command(schedule)
appointment.add_command(lookup)