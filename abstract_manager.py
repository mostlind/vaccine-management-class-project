from os import path
from pathlib import Path
from typing import Generic, List, Optional, TypeVar
import pickle
from uuid import UUID
from identifiable import Identifiable

T = TypeVar("T", bound=Identifiable)


class AbstractManager(Generic[T]):
    data_directory: str
    filename: str

    def save(self, new_item: T):
        """Create new item if it doesn't already exist, update if it does, then save to file"""

        # get all items, except the one being updated
        items = [x for x in self.all() if x.id != new_item.id]

        items.append(new_item)
        file_path = path.join(self.data_directory, self.filename)

        Path(self.data_directory).mkdir(exist_ok=True, parents=True)
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
