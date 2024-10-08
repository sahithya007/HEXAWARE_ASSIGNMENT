from abc import ABC, abstractmethod

class ILoanRepository(ABC):

    @abstractmethod
    def apply_loan(self, loan):
        """Applies for a loan, stores it in the database."""
        pass

    @abstractmethod
    def calculate_interest(self, loan_id):
        """Calculates and returns the interest for a specified loan ID."""
        pass

    @abstractmethod
    def check_and_update_loan_status(self, loan_id):
        """Checks and updates the loan status based on credit score."""
        pass

    @abstractmethod
    def get_loan_status(self, loan_id):
        """Retrieves the current status of the loan without updating it."""
        pass

    @abstractmethod
    def calculate_emi(self, loan_id):
        """Calculates and returns the EMI for the specified loan ID."""
        pass

    @abstractmethod
    def loan_repayment(self, loan_id, amount):
        """Processes loan repayment and updates the balance."""
        pass

    @abstractmethod
    def get_all_loans(self):
        """Retrieves all loans stored in the database."""
        pass

    @abstractmethod
    def get_loan_by_id(self, loan_id):
        """Retrieves a loan by its ID."""
        pass
