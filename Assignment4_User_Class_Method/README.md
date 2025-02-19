# User Class Methods  
## `User` class  
- **Purpose**: Uses information like the user ID, name, last name, email, password, and birthday to represent a user.- **Methods**:
  - `__init__(self, user_id, name, surname, email, password, birthday)`: Initializes a new user.
  - `get_details(self)`: Returns the user's details as a formatted string.
  - `get_age(self)`: Calculates and returns the user's age.  

## `UserService` Class

- **Purpose**: Maintains a user dictionary and offers tools for adding, locating, removing, and updating users.
- **Methods**:
  - `add_user(cls, user)`: Adds a user to the list.
  - `find_user(cls, user_id)`: Finds and returns a user by their ID.
  - `delete_user(cls, user_id)`: Deletes a user by their ID.
  - `update_user(cls, user_id, name, email)`: Updates a user's name and email.
  - `get_number(cls)`: Returns the number of users.  

## `UserUtil` Class

- **Purpose**: Offers useful techniques for creating user IDs, passwords, and emails as well as for email and password validation.
- **Methods**:
  - `generate_user_id()`: Generates a new user ID.
  - `generate_password()`: Generates a strong password.
  - `is_strong_password(password)`: Checks if a password is strong.
  - `generate_email(name, surname, domain)`: Generates an email address.
  - `validate_email(email)`: Validates an email address.  
## How to run the code  
1. Verify that Python is installed on your computer.
2. Make a local copy of the repository.
3. Go to the directory for the project.
4. To communicate with the user management system, execute the `sample.py` file:
   ```sh
   python sample.py
   ```  

## UML diagram  
<img width='850' alt="Снимок экрана 2025-02-19 в 00 42 18" src=https://github.com/xthimylJ/OOP_HWs/blob/main/Assignment4_User_Class_Method/UML_diagram.png>  

## Sample output  

```
User added successfully!
User_id: 259187503
Name of the user: Nazik
Surname of the user: Omurgazieva
Email of ther user:
User age: Age of the user: 19 years old
```

## Tesst output  
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```
