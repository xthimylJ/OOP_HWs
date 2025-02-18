import unittest
from datetime import datetime
import string
from userUtil import UserUtil  

class TestUserUtil(unittest.TestCase):
    
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertIsInstance(user_id, int)
        self.assertEqual(len(str(user_id)), 9)  
        self.assertTrue(str(user_id).startswith(str(datetime.now().year)[2:]))
    
    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertGreaterEqual(len(password), 8)
        self.assertLessEqual(len(password), 20)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))
    
    def test_is_strong_password(self):
        self.assertEqual(UserUtil.is_strong_password("Aa1!abcd"), "Your password is strong.")
        self.assertEqual(UserUtil.is_strong_password("weakpass"), "Your password is weak.")
        
    
    def test_generate_email(self):
        email = UserUtil.generate_email("John", "Doe", "example.com")
        self.assertEqual(email, "john.doe@example.com")
    
    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("john.doe@example.com"))
        self.assertFalse(UserUtil.validate_email("john.doeexample.com"))
        

if __name__ == "__main__":
    unittest.main()