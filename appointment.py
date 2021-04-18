from abstract_manager import AbstractManager
from datetime import datetime
from uuid import UUID, uuid4
from identifiable import Identifiable


class Appointment(Identifiable):
    def __init__(self, user_id: UUID, facility_id: UUID, date: datetime) -> None:
        self.id = uuid4()
        self.user_id = user_id
        self.facility_id = facility_id
        self.date = date


class ApppointmentManager(AbstractManager[Appointment]):
    def __init__(self, data_directory="data") -> None:
        self.filename = "appoinments.pickle"
        self.data_directory = data_directory
