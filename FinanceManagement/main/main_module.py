import sys
import os
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from dao.FinanceRepositoryImpl import FinanceRepositoryImpl
from entity.User import User
from entity.Expense import Expense
from exception.UserNotFoundException import UserNotFoundException
from exception.ExpenseNotFoundException import ExpenseNotFoundException

class FinanceManagementApp:
    def __init__(self):
        self.repo = FinanceRepositoryImpl()
        self.current_user = None

    def run(self):
        
        print("--- Finance Management App ---")
        while True:
            if self.current_user:  #To check if the user is logged in
                print(f"\n--- Logged in as {self.current_user.get_username()} ---")
                print("1. Add Expense")
                print("2. Delete Expense")
                print("3. Update Expense")
                print("4. View All Expenses")
                print("5. View Expenses by Category")
                print("6. View Expenses by Date Range")
                print("7. Logout")
                print("8. Exit")
                choice = input("Choose an option: ")

                if choice == "1":
                    self.add_expense()
                elif choice == "2":
                    self.delete_expense()
                elif choice == "3":
                    self.update_expense()
                elif choice == "4":
                    self.view_all_expenses()
                elif choice == "5":
                    self.view_expenses_by_category()
                elif choice == "6":
                    self.view_expenses_by_date_range()
                elif choice == "7":
                    self.logout()
                elif choice == "8":
                    break
                else:
                    print("Invalid choice. Please choose again.")
            else:
                print("\n--- Finance Management App Menu ---")
                print("1. Add User")
                print("2. Delete User")
                print("3. Login")
                print("4. Exit")
                choice = input("Choose an option: ")

                if choice == "1":
                    self.add_user()
                elif choice == "2":
                    self.delete_user()
                elif choice == "3":
                    self.login()
                elif choice == "4":
                    break
                else:
                    print("Invalid choice. Please choose again.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if self.repo.authenticate_user(username, password):
            self.current_user = self.repo.get_user_by_username(username)
            print(f"Logged in as {username}.")
        else:
            print("Invalid username or password.")

    def logout(self):
        print(f"User {self.current_user.get_username()} logged out.")
        self.current_user = None

    def add_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        email = input("Enter email: ")
        user = User(username=username, password=password, email=email)
        if self.repo.create_user(user):
            print("User created successfully.")
        else:
            print("Error creating user.")

    def delete_user(self):
        username = input("Enter username to delete: ")
        try:
            user = self.repo.get_user_by_username(username)
            confirm = input(f"Are you sure you want to delete the user '{user.get_username()}'? (yes/no): ")
            if confirm.lower() == "yes":
                if self.repo.delete_user(user.get_user_id()):
                    print(f"User '{username}' deleted successfully.")
                else:
                    print(f"Error deleting user '{username}'.")
        except UserNotFoundException as e:
            print(e)

    def add_expense(self):
        amount = float(input("Enter amount: "))
        category_name = input("Enter category name: ")  
        category_id = self.repo.get_category_id_by_name(category_name)
        if category_id is None:
            print(f"Category '{category_name}' does not exist.")
            return
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        expense = Expense(user_id=self.current_user.get_user_id(), amount=amount, category_id=category_id, date=date, description=description)
        if self.repo.create_expense(expense):
            print("Expense created successfully.")
        else:
            print("Error creating expense.")

    def delete_expense(self):
        expense_id = int(input("Enter expense ID to delete: "))
        try:
            if self.repo.delete_expense(expense_id):
                print("Expense deleted successfully.")
            else:
                print("Error deleting expense.")
        except ExpenseNotFoundException as e:
            print(e)

    def update_expense(self):
        expense_id = int(input("Enter expense ID to update: "))
        amount = float(input("Enter new amount: "))
        category_name = input("Enter new category name: ")  
        category_id = self.repo.get_category_id_by_name(category_name)
        if category_id is None:
            print(f"Category '{category_name}' does not exist.")
            return
        date = input("Enter new date (YYYY-MM-DD): ")
        description = input("Enter new description: ")
        expense = Expense(expense_id=expense_id, user_id=self.current_user.get_user_id(), amount=amount, category_id=category_id, date=date, description=description)
        if self.repo.update_expense(self.current_user.get_user_id(), expense):
            print("Expense updated successfully.")
        else:
            print("Error updating expense.")

    def view_all_expenses(self):
        expenses = self.repo.get_all_expenses(self.current_user.get_user_id())
        if expenses:
            for expense in expenses:
                print(f"Expense ID: {expense.get_expense_id()}, Amount: {expense.get_amount()}, Category: {expense.get_category_name()}, Date: {expense.get_date()}, Description: {expense.get_description()}")
        else:
            print("No expenses found.")

    def view_expenses_by_category(self):
        category_name = input("Enter category name: ")
        expenses = self.repo.get_expenses_by_category(self.current_user.get_user_id(), category_name)
        if expenses:
            for expense in expenses:
                print(f"Expense ID: {expense.get_expense_id()}, Amount: {expense.get_amount()}, Date: {expense.get_date()}, Description: {expense.get_description()}")
        else:
            print(f"No expenses found in category '{category_name}'.")

    def view_expenses_by_date_range(self):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        expenses = self.repo.get_expenses_between_dates(self.current_user.get_user_id(), start_date, end_date)
        if expenses:
            for expense in expenses:
                print(f"Expense ID: {expense.get_expense_id()}, Amount: {expense.get_amount()}, Category: {expense.get_category_name()}, Date: {expense.get_date()}, Description: {expense.get_description()}")
        else:
            print(f"No expenses found between {start_date} and {end_date}.")

if __name__ == "__main__":
    app = FinanceManagementApp()
    app.run()
