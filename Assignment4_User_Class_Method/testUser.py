import unittest # import unittest framework
from user import User # from user.py file (module) import User class

class TestUser(unittest.TestCase): # class TestUser inherints all the stuff from TestCase Class
    def setUp(self):
        
        self.test_user = User(1, "Nazik", "Omurgazieva", "21 April 2005")
    
    def test_get_details(self):
        
        expected_output = (
            "User_id: 1\n"
            "Name of the user: Nazik\n"
            "Surname of the user: Omurgazieva\n"
            "Email of ther user: "
        )
        self.assertEqual(self.test_user.get_details(), expected_output)

    def test_get_age(self):
        age_str = self.test_user.get_age()
        expected_output = "Age of the user: 19 years old"
        self.assertEqual(age_str, expected_output)

if __name__ == "__main__":
    unittest.main()