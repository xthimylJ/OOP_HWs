import random # importing the whole module
from datetime import datetime # importing "datemite" class from "datetime" module
import string # 
import re

class UserUtil:

    @staticmethod
    def generate_user_id(): 
        password = ""
        current_year = str(datetime.now().year)
        password += current_year[2:]
        i = 1
        while i <= 7:
            password += str(random.randint(0, 9))
            i += 1
        return int(password)
    
    @staticmethod
    def generate_password():
        symbols = string.punctuation # module.variable -> "string.punctuation"
                                     # we assign string module variable "punctuation" to local 
                                     # variable "symbols"
        lowercase_letters = 'abcdefjhigklmnopqrstuvwxyz'
        uppercase_letters = lowercase_letters.upper()
        digits = '0123456789'
        all = symbols + lowercase_letters + uppercase_letters + digits
        pwd = ""
        min_len = random.randint(8, 20)
        meet_criteria = False 
        has_lower = False
        has_uppercase = False
        has_digits = False
        has_special = False

        while not meet_criteria or len(pwd) < min_len:
            new_char = random.choice(all)
            pwd += new_char
            if new_char in lowercase_letters:
                has_lower = True
            elif new_char in uppercase_letters:
                has_uppercase = True
            elif new_char in digits:
                has_digits = True
            elif new_char in symbols:
                has_special = True
            
            if has_lower and has_uppercase and has_digits and has_special:
                meet_criteria = True
        #print('Your password: ', end='')
        return pwd
    
    @staticmethod

    def is_strong_password(password: str):
        min_len = 8
        symbols = string.punctuation
        uppercase = 'abcdefjhigklmnopqrstuvwxyz'.upper()
        digits = '0123456789'
        meets_criteria = False
        has_upper = False
        has_digits = False 
        has_syms = False

        for i in password:
            if i in uppercase:
                has_upper = True
            if i in digits:
                has_digits = True
            if i in symbols: 
                has_syms = True
        if has_syms and has_digits and has_upper:
            meets_criteria = True
        

        if meets_criteria and len(password) >= min_len:
            return f"Your password is strong."
        else:
            return f"Your password is weak."
        
    @staticmethod 
    def generate_email(name: str, surname: str, domain: str): 
        return name.lower() + '.' + surname.lower() + '@' + domain.lower()

    @staticmethod
    def validate_email(email: str):
        pattern = r"^[a-zA-Z]+\.[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
        return bool(re.fullmatch(pattern, email))

