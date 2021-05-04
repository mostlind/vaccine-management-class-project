from datetime import date
from uuid import UUID, uuid4
from entities.identifiable import Identifiable
from entities.abstract_manager import AbstractManager


class User(Identifiable):
    def __init__(
        self,
        name: str,
        date_of_birth: date,
        address: str,
        number_of_preexisting_conditions: int,
    ) -> None:
        self.id = uuid4()
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.number_of_preexisting_conditions = number_of_preexisting_conditions


class UserManager(AbstractManager[User]):
    def __init__(self, data_directory="data") -> None:
        self.filename = "users.pickle"
        self.data_directory = data_directory
