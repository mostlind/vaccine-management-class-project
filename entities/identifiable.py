from uuid import UUID


class Identifiable:
    id: UUID

    def __eq__(self, o: object) -> bool:
        return self.id == o.id
