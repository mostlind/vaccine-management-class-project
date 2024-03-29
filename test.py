from datetime import date
from entities.user import User
from entities.facility import Facility
from click.testing import CliRunner
from cli import cli
import unittest


def contains(string: str, substring: str):
    return string.find(substring) != -1


class IntegrationTest(unittest.TestCase):
    def test_register_facility(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            runner.invoke(
                cli,
                ["facility", "register"],
                input="CVS\n123 Address Street\n1000",
            )

            facilities = runner.invoke(cli, ["facility", "list"])

            facility_id = str(facilities.output).splitlines()[1].split(",")[0]

            result = runner.invoke(cli, ["facility", "lookup", "--id", facility_id])

            self.assertTrue(contains(str(result.output), "CVS"))
            self.assertTrue(contains(str(result.output), "123 Address Street"))
            self.assertTrue(contains(str(result.output), "1000"))

    def test_schedule_appointment(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            facility_name = "CVS"
            user_name = "Alice Smith"
            runner.invoke(
                cli,
                ["facility", "register"],
                input=f"{facility_name}\n123 Address Street\n1000",
            )

            facilities = runner.invoke(cli, ["facility", "list"])

            facility_id = str(facilities.output).splitlines()[1].split(",")[0]

            appointment_created = runner.invoke(
                cli,
                ["appointment", "schedule"],
                input=f"{user_name}\n456 Road Blvd\n1990-01-01\n3\n{facility_id}",
            )

            self.assertEqual(appointment_created.exit_code, 0)
            self.assertTrue(
                contains(str(appointment_created.output), "Appoinment scheduled")
            )

            appointments = runner.invoke(cli, ["appointment", "list"])
            appointment_id = str(appointments.output).splitlines()[1].split(",")[0]

            appointment = runner.invoke(
                cli, ["appointment", "lookup", "--id", appointment_id]
            )

            appoinment_output = str(appointment.output)

            self.assertEqual(appointment.exit_code, 0)
            self.assertTrue(contains(appoinment_output, f"Id: {appointment_id}"))
            self.assertTrue(contains(appoinment_output, f"Facility: {facility_name}"))
            self.assertTrue(contains(appoinment_output, f"User: {user_name}"))

    def test_equality_defined_in_super_class(self):
        facility_1 = Facility("1", "1", 1)
        facility_2 = Facility("2", "2", 2)

        self.assertNotEqual(facility_1, facility_2)
        facility_2.id = facility_1.id
        self.assertEqual(facility_1, facility_2)

        today = date.today()
        user_1 = User("1", today, "1", 1)
        user_2 = User("2", today, "2", 2)

        self.assertNotEqual(user_1, user_2)
        user_2.id = user_1.id
        self.assertEqual(user_1, user_2)


if __name__ == "__main__":
    unittest.main()
