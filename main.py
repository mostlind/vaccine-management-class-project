import click
from cli.facility import facility
from cli.appointment import appointment

# user_manager = UserManager()
# user = User("sam", datetime.date.today(), "123 address street", 1)
# user_manager.save(user)

# print([x.id for x in user_manager.all()])


@click.group()
def cli():
    pass


cli.add_command(facility)
cli.add_command(appointment)

cli()