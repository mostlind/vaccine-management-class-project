from uuid import uuid4
from facility import Facility
import unittest
import os
from facility import Facility, FacilityManager
import shutil


class UserTest(unittest.TestCase):
    # generate random filename
    data_directory = str(uuid4())

    def setUp(self) -> None:
        os.mkdir(self.data_directory)

    def test_integration(self):
        facility_manager = FacilityManager(data_directory=self.data_directory)
        test_facility = Facility(
            name="Local Pharmacy", address="123 street street", number_of_vaccines=3
        )
        facility_manager.save(test_facility)
        facilities = facility_manager.all()

        self.assertEqual(test_facility, facilities[0])

    def tearDown(self) -> None:
        shutil.rmtree(self.data_directory)
