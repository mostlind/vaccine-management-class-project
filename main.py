from uuid import uuid4
from user import UserManager, User
import datetime

user_manager = UserManager()
user = User("sam", datetime.date.today(), "123 address street", 1)
user_manager.save(user)

print([x.id for x in user_manager.all()])