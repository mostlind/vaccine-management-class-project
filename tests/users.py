import unittest
import os
from uuid import uuid4
from user import User, UserManager
from datetime import date
import shutil


class UserTest(unittest.TestCase):
    # generate random data directory
    data_directory = str(uuid4())

    def setUp(self) -> None:
        os.mkdir(self.data_directory)

    def test_integration(self):
        user_manager = UserManager(data_directory=self.data_directory)
        test_user = User(
            name="Sam",
            date_of_birth=date.today(),
            address="123 street street",
            number_of_preexisting_conditions=3,
        )
        user_manager.save(test_user)
        users = user_manager.all()

        self.assertEqual(test_user, users[0])

    def tearDown(self) -> None:
        shutil.rmtree(self.data_directory)
