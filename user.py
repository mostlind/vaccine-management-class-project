from datetime import date


class User:
    name: str
    dateOfBirth: date
    address: str
    numbeOfPreexistingConditions: int

    def __init__(
        self,
        name: str,
        dateOfBirth: date,
        address: str,
        numbeOfPreexistingConditions: int,
    ) -> None:
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.numbeOfPreexistingConditions = numbeOfPreexistingConditions
