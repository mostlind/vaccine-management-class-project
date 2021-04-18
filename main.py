import user
from user_manager import UserManager
import datetime

user = user.User("sam", datetime.date.today(), "123 address street", 1)
UserManager.save(user)

print(UserManager.all())