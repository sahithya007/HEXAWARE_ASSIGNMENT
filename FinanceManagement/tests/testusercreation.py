import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

import unittest

from dao.FinanceRepositoryImpl import FinanceRepositoryImpl
from entity.User import User

class TestUserCreation(unittest.TestCase):

    def setUp(self):
        self.repo = FinanceRepositoryImpl()

    def test_user_creation(self):
      
        new_user = User(username="test_user", password="password123", email="test_user@example.com")
        success = self.repo.create_user(new_user)
        
        fetched_user = self.repo.get_user_by_username("test_user")

        self.assertTrue(success)
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.get_username(), "test_user")

    def tearDown(self):
        test_user = self.repo.get_user_by_username("test_user")
        if test_user:
            self.repo.delete_user(test_user.get_user_id())

if __name__ == '__main__':
    unittest.main()
