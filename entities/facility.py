from uuid import UUID, uuid4
from entities.identifiable import Identifiable
from entities.abstract_manager import AbstractManager


class Facility(Identifiable):
    def __init__(
        self,
        name: str,
        address: str,
        number_of_vaccines: int,
    ) -> None:
        self.id = uuid4()
        self.name = name
        self.address = address
        self.number_of_vaccines = number_of_vaccines


class FacilityManager(AbstractManager[Facility]):
    def __init__(self, data_directory="data") -> None:
        self.filename = "facilities.pickle"
        self.data_directory = data_directory