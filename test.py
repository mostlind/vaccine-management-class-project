from click.testing import CliRunner
from cli import cli
import unittest


class IntegrationTest(unittest.TestCase):
    def test_integration(self):
        runner = CliRunner()
        with runner.isolated_filesystem():
            runner.invoke(
                cli,
                ["facility", "register"],
                input="Facility Name\n123 Address Street\n1000",
            )

            result = runner.invoke(cli, ["facility", "list"])

            self.assertEqual(
                str(result.output).splitlines()[1].split(",")[1],
                "Facility Name",
            )


if __name__ == "__main__":
    unittest.main()
