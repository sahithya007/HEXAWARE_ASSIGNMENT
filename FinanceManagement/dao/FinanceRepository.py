from abc import ABC, abstractmethod

class FinanceRepository(ABC):
    
    @abstractmethod
    def authenticate_user(self, username, password):
        """Authenticates a user with the given username and password."""
        pass

    @abstractmethod
    def create_user(self, user):
        """Creates a new user in the database."""
        pass

    @abstractmethod
    def get_user_by_username(self, username):
        """Retrieves a user from the database by their username."""
        pass

    @abstractmethod
    def create_expense(self, expense):
        """Creates a new expense in the database."""
        pass

    @abstractmethod
    def delete_user(self, user_id):
        """Deletes a user from the database along with all related expenses."""
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

    @abstractmethod
    def get_category_id_by_name(self, category_name):
        """Retrieves the category ID based on the category name."""
        pass

    @abstractmethod
    def get_expenses_by_category(self, user_id, category_name):
        """Fetches all expenses for a user that belong to a particular category."""
        pass

    @abstractmethod
    def get_expenses_between_dates(self, user_id, start_date, end_date):
        """Fetches all expenses for a user between two dates."""
        pass
