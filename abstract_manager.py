from os import path
from typing import Generic, List, Optional, TypeVar
import pickle
from uuid import UUID
from identifiable import Identifiable

T = TypeVar("T", bound=Identifiable)


class AbstractManager(Generic[T]):
    data_directory: str
    filename: str

    def save(self, item: T):
        items = self.all()
        items.append(item)
        file_path = path.join(self.data_directory, self.filename)

        with open(file_path, "wb+") as f:
            pickle.dump(items, f)

    def all(self) -> List[T]:
        try:
            file_path = path.join(self.data_directory, self.filename)
            with open(file_path, "rb") as f:
                return pickle.load(f)
        except:
            return []

    def find_by_id(self, id: UUID) -> Optional[T]:
        items = self.read_from_file()
        for item in items:
            if item.id == id:
                return item
        return None
