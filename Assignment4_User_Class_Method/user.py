from datetime import datetime
import userUtil 
class User:
    def __init__(self, user_id: int, name: str, surname: str, birthday: str):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        birthday_date = datetime.strptime(birthday, "%d %B %Y").date()
        self.birthday = birthday_date
        self.email: str = ""
        self.password: str = userUtil.UserUtil.generate_password()
    
    # instance method
    def get_details(self): # we don't need to pass anything when call this method: just obj.get_detail()
        return f"User_id: {self.user_id}\n" \
               f"Name of the user: {self.name}\n" \
               f"Surname of the user: {self.surname}\n" \
               f"Email of ther user: {self.email}" 
    
    # instance method 
    def get_age(self):
        today = datetime.today().date() # variable "today" type is datetime class object
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return f"Age of the user: {age} years old"

    # representing as a string and not as memory address

    def __str__(self): # we don't pass anything here
        return self.get_details()
        


