import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

import unittest
from entity.Expense import Expense
from entity.User import User
from dao.FinanceRepositoryImpl import FinanceRepositoryImpl


class TestSearchExpense(unittest.TestCase):

    def setUp(self):
        self.repo = FinanceRepositoryImpl()
        self.test_user = User(username="search_user", password="password123", email="search_user@example.com")
        self.repo.create_user(self.test_user)
        self.test_user = self.repo.get_user_by_username("search_user")
        category_id = self.repo.get_category_id_by_name("Utilities")
        self.expense = Expense(user_id=self.test_user.get_user_id(), amount=50, category_id=category_id, date="2024-10-11", description="Electricity Bill")
        self.repo.create_expense(self.expense)

    def test_search_expense(self):
        expenses = self.repo.get_all_expenses(self.test_user.get_user_id())
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].get_description(), "Electricity Bill")

    def tearDown(self):
        expenses = self.repo.get_all_expenses(self.test_user.get_user_id())
        for expense in expenses:
            self.repo.delete_expense(expense.get_expense_id())
        self.repo.delete_user(self.test_user.get_user_id())

if __name__ == '__main__':
    unittest.main()
