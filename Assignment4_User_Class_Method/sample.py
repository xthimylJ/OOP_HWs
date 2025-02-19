from user import User
from userService import UserService
from userUtil import UserUtil

user_id = UserUtil.generate_user_id()
name = input("Enter your name: ")
surname = input("Enter your surname: ")
birthday = input("Your date of birth: ")

user = User(user_id, name, surname, birthday)
UserService.add_user(user)

print(f"User added successfully! \n{user.get_details()}")

print(f"User age: {user.get_age()}")