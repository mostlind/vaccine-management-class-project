from typing import List
from user import User
import pickle

users_file = "users.pickle"


class UserManager:
    @staticmethod
    def save(user: User):
        users = UserManager.all_users()

        users.append(user)
        print(users)
        UserManager.__write_to_file(users)

    @staticmethod
    def all() -> List[User]:
        try:
            return UserManager.__read_from_file()
        except IOError:
            return []

    @staticmethod
    def __write_to_file(users: List[User]):
        with open(users_file, "wb+") as f:
            pickle.dump(users, f)

    @staticmethod
    def __read_from_file():
        users = []

        with open(users_file, "rb") as f:
            users = pickle.load(f)

        return users
