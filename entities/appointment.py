from entities.abstract_manager import AbstractManager
from datetime import date as date_type
from uuid import UUID, uuid4
from entities.identifiable import Identifiable


class Appointment(Identifiable):
    def __init__(self, user_id: UUID, facility_id: UUID, date: date_type) -> None:
        self.id = uuid4()
        self.user_id = user_id
        self.facility_id = facility_id
        self.date = date


class ApppointmentManager(AbstractManager[Appointment]):
    def __init__(self, data_directory="data") -> None:
        self.filename = "appointments.pickle"
        self.data_directory = data_directory
