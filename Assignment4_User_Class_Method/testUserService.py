import unittest
from userService import UserService
from user import User

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user1 = User(1, "Nazik", "Omurgazieva", "21 April 2005")
        self.user2 = User(2, "Amina", "Omurgazieva", "19 June 2010")
        self.user3 = User(3, "Emirhan", "Omurgaziev", "29 November 2017")
    
    def test_add_user(self):
        UserService.add_user(self.user1)
        UserService.add_user(self.user2)
        self.assertEqual(len(UserService.users), 2)

    def test_find_user(self):
        found_user = UserService.find_user(1)
        self.assertEqual(found_user.user_id, self.user1.user_id)

    def test_delete_user(self):
        UserService.delete_user(2)
        self.assertEqual(len(UserService.users), 1)
    
    def test_update_user(self):
        UserService.update_user(1, self.user3)
        
        su_n = self.user3.name
        self.assertEqual(UserService.users[1].name, su_n)

    def test_get_number(self):
        ret_str = "Number of users: 1"
        
        self.assertEqual(UserService.get_number(), ret_str)


if __name__ == "__main__":
    unittest.main()