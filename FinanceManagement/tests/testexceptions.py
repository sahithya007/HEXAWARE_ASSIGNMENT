import sys
import os
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
import unittest
from dao.FinanceRepositoryImpl import FinanceRepositoryImpl
from exception.UserNotFoundException import UserNotFoundException
from exception.ExpenseNotFoundException import ExpenseNotFoundException

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

class TestExceptions(unittest.TestCase):
    
    def setUp(self):
        self.repo = FinanceRepositoryImpl()

    def test_user_not_found_exception(self):
        with self.assertRaises(UserNotFoundException):
            self.repo.get_user_by_username("non_existent_user")

    def test_expense_not_found_exception(self):
        with self.assertRaises(ExpenseNotFoundException):
            self.repo.delete_expense(99999)

if __name__ == '__main__':
    unittest.main()
