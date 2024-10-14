import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

import unittest
from entity.Expense import Expense
from entity.User import User
from dao.FinanceRepositoryImpl import FinanceRepositoryImpl

class TestExpenseCreation(unittest.TestCase):

    def setUp(self):
        self.repo = FinanceRepositoryImpl()
        self.test_user = User(username="expense_user", password="password123", email="expense_user@example.com")
        self.repo.create_user(self.test_user)
        self.test_user = self.repo.get_user_by_username("expense_user")

    def test_expense_creation(self):
        category_id = self.repo.get_category_id_by_name("Food")
        new_expense = Expense(user_id=self.test_user.get_user_id(), amount=1000, category_id=category_id, date="2024-10-11", description="Dinner")
        success = self.repo.create_expense(new_expense)
        
        expenses = self.repo.get_all_expenses(self.test_user.get_user_id())
        
        self.assertTrue(success)
        self.assertGreater(len(expenses), 0)
        self.assertEqual(expenses[0].get_description(), "Dinner")

    def tearDown(self):
        expenses = self.repo.get_all_expenses(self.test_user.get_user_id())
        for expense in expenses:
            self.repo.delete_expense(expense.get_expense_id())
        self.repo.delete_user(self.test_user.get_user_id())

if __name__ == "__main__":
    unittest.main()
