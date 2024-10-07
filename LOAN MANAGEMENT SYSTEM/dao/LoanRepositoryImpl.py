import sys
sys.path.append(r"C:\Users\SAHITHYA\OneDrive\Desktop\LOAN MANAGEMENT SYSTEM")
from dao.ILoanRepository import ILoanRepository
from exception.InvalidLoanException import InvalidLoanException

class LoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.loans = {}  # Simulating a database with a dictionary
        self.next_loan_id = 1  # Initialize loan ID counter

    def apply_loan(self, loan):
        confirmation = input("Do you want to apply for this loan? (Yes/No): ")
        if confirmation.lower() == 'yes':
            loan.loan_id = self.next_loan_id  # Assign the current loan ID
            loan.loan_status = "Pending"
            self.loans[loan.loan_id] = loan
            print(f"Loan application submitted with ID: {loan.loan_id}")
            self.next_loan_id += 1  # Increment for the next loan ID
        else:
            print("Loan application canceled.")

    def calculate_interest(self, loan_id):
        loan = self.get_loan_by_id(loan_id)
        if loan:
            interest = (loan.principal_amount * loan.interest_rate * loan.loan_term) / 12
            return interest
        else:
            raise InvalidLoanException(f"Loan with ID {loan_id} not found.")

    def loan_status(self, loan_id):
        loan = self.get_loan_by_id(loan_id)
        if loan:
            if loan.customer.credit_score > 650:
                loan.loan_status = "Approved"
            else:
                loan.loan_status = "Rejected"
            print(f"Loan status for ID {loan_id}: {loan.loan_status}")
        else:
            raise InvalidLoanException(f"Loan with ID {loan_id} not found.")

    def calculate_emi(self, loan_id):
        loan = self.get_loan_by_id(loan_id)
        if loan:
            P = loan.principal_amount
            R = loan.interest_rate / 12 / 100
            N = loan.loan_term
            emi = (P * R * (1 + R)**N) / ((1 + R)**N - 1)
            return emi
        else:
            raise InvalidLoanException(f"Loan with ID {loan_id} not found.")

    def loan_repayment(self, loan_id, amount):
        loan = self.get_loan_by_id(loan_id)
        if loan:
            emi = self.calculate_emi(loan_id)
            if amount < emi:
                print("Repayment rejected. Amount is less than the EMI.")
            else:
                # Update repayment logic (e.g., reduce outstanding balance, etc.)
                print(f"Repayment of {amount} accepted for loan ID {loan_id}.")
        else:
            raise InvalidLoanException(f"Loan with ID {loan_id} not found.")

    def get_all_loans(self):
        return list(self.loans.values())

    def get_loan_by_id(self, loan_id):
        loan = self.loans.get(loan_id, None)
        if loan:
            return loan
        else:
            raise InvalidLoanException(f"Loan with ID {loan_id} not found.")
