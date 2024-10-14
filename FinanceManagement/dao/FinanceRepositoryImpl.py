from dao.FinanceRepository import FinanceRepository
from util.DBConnUtil import DBConnUtil
from exception.UserNotFoundException import UserNotFoundException
from exception.ExpenseNotFoundException import ExpenseNotFoundException
from entity.User import User
from entity.Expense import Expense

class FinanceRepositoryImpl(FinanceRepository):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def authenticate_user(self, username, password):
        self.cursor.execute("SELECT * FROM Users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()
        return user is not None

    def get_user_by_username(self, username):
        sql = "SELECT * FROM Users WHERE username = ?"
        self.cursor.execute(sql, (username,))
        row = self.cursor.fetchone()

        if row:
            user = User(
                user_id=row.user_id,
                username=row.username,
                password=row.password,
                email=row.email
            )
            return user
        else:
            raise UserNotFoundException(f"User with username '{username}' not found.")

    def create_user(self, user):
        try:
            sql = "INSERT INTO Users (username, password, email) VALUES (?, ?, ?)"
            self.cursor.execute(sql, (user.get_username(), user.get_password(), user.get_email()))
            self.conn.commit()
            return True
        except Exception as e:
            return False

    def get_category_id_by_name(self, category_name):
        sql = "SELECT category_id FROM ExpenseCategories WHERE category_name = ?"
        self.cursor.execute(sql, (category_name,))
        row = self.cursor.fetchone()
        return row.category_id if row else None

    def create_expense(self, expense):
        try:
            sql = """
            INSERT INTO Expenses (user_id, amount, category_id, date, description)
            VALUES (?, ?, ?, ?, ?)
            """
            self.cursor.execute(
                sql,
                (expense.get_user_id(), expense.get_amount(), expense.get_category_id(), 
                 expense.get_date(), expense.get_description())
            )
            self.conn.commit()
            return True
        except Exception as e:
            return False

    def delete_user(self, user_id):
        try:
            self.cursor.execute("SELECT user_id FROM Users WHERE user_id = ?", (user_id,))
            result = self.cursor.fetchone()
            if result is None:
                raise UserNotFoundException(f"User with ID {user_id} not found.")
            
            self.cursor.execute("DELETE FROM Expenses WHERE user_id = ?", (user_id,))
            self.cursor.execute("DELETE FROM Users WHERE user_id = ?", (user_id,))
            self.conn.commit()
            return True
        except UserNotFoundException:
            return False
        except Exception as e:
            return False

    def delete_expense(self, expense_id):
        try:
            self.cursor.execute("SELECT expense_id FROM Expenses WHERE expense_id = ?", (expense_id,))
            result = self.cursor.fetchone()
            if result is None:
                raise ExpenseNotFoundException(f"Expense with ID {expense_id} not found.")
            
            self.cursor.execute("DELETE FROM Expenses WHERE expense_id = ?", (expense_id,))
            self.conn.commit()
            return True
        except ExpenseNotFoundException:
            raise
        except Exception as e:
            return False

    def get_all_expenses(self, user_id):
        sql = """
        SELECT e.expense_id, e.amount, c.category_name, e.date, e.description
        FROM Expenses e
        JOIN ExpenseCategories c ON e.category_id = c.category_id
        WHERE e.user_id = ?
        """
        self.cursor.execute(sql, (user_id,))
        rows = self.cursor.fetchall()
        expenses = []
        for row in rows:
            expense = Expense(
                expense_id=row.expense_id,
                user_id=user_id,
                amount=row.amount,
                category_name=row.category_name,  
                date=row.date,
                description=row.description
            )
            expenses.append(expense)
        return expenses

    def update_expense(self, user_id, expense):
        try:
            sql_check = "SELECT expense_id FROM Expenses WHERE expense_id = ? AND user_id = ?"
            self.cursor.execute(sql_check, (expense.get_expense_id(), user_id))
            result = self.cursor.fetchone()
            if result is None:
                raise ExpenseNotFoundException(f"Expense with ID {expense.get_expense_id()} not found for user ID {user_id}.")

            sql_update = """
            UPDATE Expenses
            SET amount = ?, category_id = ?, date = ?, description = ?
            WHERE expense_id = ?
            """
            self.cursor.execute(
                sql_update,
                (expense.get_amount(), expense.get_category_id(), expense.get_date(), 
                 expense.get_description(), expense.get_expense_id())
            )
            self.conn.commit()
            return True
        except ExpenseNotFoundException:
            return False
        except Exception as e:
            return False

    def get_expenses_by_category(self, user_id, category_name):
        sql = """
        SELECT e.expense_id, e.amount, c.category_name, e.date, e.description
        FROM Expenses e
        JOIN ExpenseCategories c ON e.category_id = c.category_id
        WHERE e.user_id = ? AND c.category_name = ?
        """
        self.cursor.execute(sql, (user_id, category_name))
        rows = self.cursor.fetchall()
        expenses = []
        for row in rows:
            expense = Expense(
                expense_id=row.expense_id,
                user_id=user_id,
                amount=row.amount,
                category_name=row.category_name,
                date=row.date,
                description=row.description
            )
            expenses.append(expense)
        return expenses

    def get_expenses_between_dates(self, user_id, start_date, end_date):
        sql = """
        SELECT e.expense_id, e.amount, c.category_name, e.date, e.description
        FROM Expenses e
        JOIN ExpenseCategories c ON e.category_id = c.category_id
        WHERE e.user_id = ? AND e.date BETWEEN ? AND ?
        """
        self.cursor.execute(sql, (user_id, start_date, end_date))
        rows = self.cursor.fetchall()
        expenses = []
        for row in rows:
            expense = Expense(
                expense_id=row.expense_id,
                user_id=user_id,
                amount=row.amount,
                category_name=row.category_name,
                date=row.date,
                description=row.description
            )
            expenses.append(expense)
        return expenses
