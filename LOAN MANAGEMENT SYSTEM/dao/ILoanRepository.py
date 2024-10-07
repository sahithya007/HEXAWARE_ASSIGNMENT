from abc import ABC, abstractmethod

class ILoanRepository(ABC):

    @abstractmethod
    def apply_loan(self, loan):
        """Applies for a loan, stores it in the database."""
        pass

    @abstractmethod
    def calculate_interest(self, loan_id):
        """Calculates interest for a loan."""
        pass

    @abstractmethod
    def loan_status(self, loan_id):
        """Checks and updates the loan status based on credit score."""
        pass

    @abstractmethod
    def calculate_emi(self, loan_id):
        """Calculates EMI for the loan."""
        pass

    @abstractmethod
    def loan_repayment(self, loan_id, amount):
        """Processes loan repayment and updates the balance."""
        pass

    @abstractmethod
    def get_all_loans(self):
        """Retrieves all loans."""
        pass

    @abstractmethod
    def get_loan_by_id(self, loan_id):
        """Retrieves a loan by ID."""
        pass
