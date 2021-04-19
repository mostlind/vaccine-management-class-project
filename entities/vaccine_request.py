from entities.abstract_manager import AbstractManager
from uuid import UUID, uuid4
from entities.identifiable import Identifiable


class VaccineRequest(Identifiable):
    def __init__(self, facility_id: UUID, number_of_vaccines: int) -> None:
        self.id = uuid4()
        self.facility_id = facility_id
        self.number_of_vaccines = number_of_vaccines


class VaccineRequestManager(AbstractManager[VaccineRequest]):
    def __init__(self, data_directory="data") -> None:
        self.filename = "vaccine_requests.pickle"
        self.data_directory = data_directory
