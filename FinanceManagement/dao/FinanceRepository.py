from abc import ABC,abstractmethod

class FinanceRepository(ABC):
    @abstractmethod
    def create_user(self, user):
        """Creates a new user in the database."""
        pass

    @abstractmethod
    def create_expense(self, expense):
        """Creates a new expense in the database."""
        pass

    @abstractmethod
    def delete_user(self, user_id):
        """Deletes a user from the database."""
        pass

    @abstractmethod
    def delete_expense(self, expense_id):
        """Deletes an expense from the database."""
        pass

    @abstractmethod
    def get_all_expenses(self, user_id):
        """Retrieves all expenses for a specific user."""
        pass

    @abstractmethod
    def update_expense(self, user_id, expense):
        """Updates an existing expense in the database."""
        pass
