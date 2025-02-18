from user import User

class UserService:

    # class attributes/variables
    users = {}

    # class method 
    @classmethod
    def add_user(cls, user: User): # when calling: UserService.add_user(user): 
                                   # here inside the parentheses we should pass User class object
        cls.users[user.user_id] = user
        # this function actually returns nothing 

    # class method
    @classmethod
    def find_user(cls, user_id): # UserService.find_user(user_id) -> calling
                                 # should pass int value -> user_id
        return cls.users[user_id]
    
    # class method 
    @classmethod
    def delete_user(cls, user_id): # example: UserService.delete_user('1234')
        del cls.users[user_id]
        
    
    # class method
    @classmethod 
    def update_user(cls, user_id, user_update:User): # should pass the id of the user whose attribute
                                                # you want to change -> user_id
                                                # user_update: User class object
        obj_to_change = cls.users[user_id]
        obj_to_change.name = user_update.name
        obj_to_change.surname = user_update.surname
        cls.users[user_id]=obj_to_change 

    # class method
    @classmethod
    def get_number(cls): # do not pass anything here
        return f"Number of users: {len(cls.users)}"
    

