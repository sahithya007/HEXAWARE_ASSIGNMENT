import sys
sys.path.append(r"C:\Users\SAHITHYA\OneDrive\Desktop\LOAN MANAGEMENT SYSTEM")

from dao.LoanRepositoryImpl import LoanRepositoryImpl
from entity.Customer import Customer
from entity.HomeLoan import HomeLoan
from entity.CarLoan import CarLoan
from exception.InvalidLoanException import InvalidLoanException


def menu():
    print("--- Loan Management System ---")
    print("1. Apply for Loan")
    print("2. Get All Loans")
    print("3. Get Loan by ID")
    print("4. Loan Repayment")
    print("5. Calculate EMI")
    print("6. Calculate Interest")
    print("7. Check Loan Status")
    print("8. Exit")


def calculate_emi(loan_repository):
    loan_id = int(input("Enter Loan ID: "))
    try:
        emi = loan_repository.calculate_emi(loan_id)  # Call calculate_emi method from repository
        print(f"EMI for Loan ID {loan_id} is: {emi:.2f}")  # Display the EMI amount
    except InvalidLoanException as e:
        print(e)


class LoanManagement:
    def __init__(self):
        self.loan_repo = LoanRepositoryImpl()

    def apply_loan(self):
        loan_type = input("Enter loan type (HomeLoan/CarLoan): ")
        customer_id = int(input("Enter Customer ID: "))
        customer = Customer(customer_id, "Sample Name", "email@example.com", "1234567890", "Sample Address", 700)  # Mock customer data

        principal_amount = float(input("Enter principal amount: "))
        interest_rate = float(input("Enter interest rate: "))
        loan_term = int(input("Enter loan term (months): "))

        if loan_type.lower() == "homeloan":
            property_address = input("Enter property address: ")
            property_value = float(input("Enter property value: "))
            loan = HomeLoan(0, customer, principal_amount, interest_rate, loan_term, property_address, property_value)
        elif loan_type.lower() == "carloan":
            car_model = input("Enter car model: ")
            car_value = float(input("Enter car value: "))
            loan = CarLoan(0, customer, principal_amount, interest_rate, loan_term, car_model, car_value)
        else:
            print("Invalid loan type.")
            return

        self.loan_repo.apply_loan(loan)

    def get_all_loans(self):
        loans = self.loan_repo.get_all_loans()
        for loan in loans:
            print(loan)

    def get_loan_by_id(self):
        loan_id = int(input("Enter loan ID: "))
        try:
            loan = self.loan_repo.get_loan_by_id(loan_id)
            print(loan)  # Print the loan details
        except InvalidLoanException as e:
            print(e)

    def loan_repayment(self):
        loan_id = int(input("Enter Loan ID: "))
        amount = float(input("Enter repayment amount: "))
        try:
            self.loan_repo.loan_repayment(loan_id, amount)
            print("Repayment processed successfully.")
        except InvalidLoanException as e:
            print(e)

    def calculate_interest(self):
        loan_id = int(input("Enter Loan ID: "))
        try:
            interest = self.loan_repo.calculate_interest(loan_id)
            print(f"Interest for Loan ID {loan_id} is: {interest:.2f}")
        except InvalidLoanException as e:
            print(e)

    def check_loan_status(self):
        loan_id = int(input("Enter Loan ID: "))
        try:
            loan = self.loan_repo.get_loan_by_id(loan_id)
            print(f"Loan Status for Loan ID {loan_id} is: {loan.loan_status}")
        except InvalidLoanException as e:
            print(e)

    def run(self):
        while True:
            menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.apply_loan()
            elif choice == '2':
                self.get_all_loans()
            elif choice == '3':
                self.get_loan_by_id()
            elif choice == '4':
                self.loan_repayment()
            elif choice == '5':
                calculate_emi(self.loan_repo)  # Calculate EMI
            elif choice == '6':
                self.calculate_interest()  # Calculate Interest
            elif choice == '7':
                self.check_loan_status()  # Check Loan Status
            elif choice == '8':
                print("Exiting the Loan Management System.")
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    loan_management_system = LoanManagement()
    loan_management_system.run()


if __name__ == "__main__":
    main()
