import sys
sys.path.append(r"C:\Users\SAHITHYA\OneDrive\Desktop\LOAN MANAGEMENT SYSTEM")
from dao.ILoanRepository import ILoanRepository
from exception.InvalidLoanException import InvalidLoanException
from entity.Customer import Customer 
def apply_loan(self):
    loan_type = input("Enter loan type (HomeLoan/CarLoan): ")
    customer_id = int(input("Enter Customer ID: "))
    
    # Retrieve actual customer data from your repository or data structure
    customer = self.loan_repo.get_customer_by_id(customer_id)  # Fetch customer data
    
    if not customer:
        print("Customer not found!")
        return

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
class LoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.loans = {}  # Simulating a database with a dictionary
        self.customers = {
            1: Customer(1, 'Rahul Sharma', 'rahul.sharma@example.com', '9876543210', '1st Main, Bangalore', 720),
            2: Customer(2, 'Anita Desai', 'anita.desai@example.com', '8765432109', '2nd Cross, Mumbai', 680),
            3: Customer(3, 'Vikram Singh', 'vikram.singh@example.com', '7654321098', '3rd Street, Delhi', 750),
            4: Customer(4, 'Priya Iyer', 'priya.iyer@example.com', '6543210987', '4th Lane, Chennai', 800),
            5: Customer(5, 'Ravi Patel', 'ravi.patel@example.com', '5432109876', '5th Road, Ahmedabad', 660),
            6: Customer(6, 'Sneha Nair', 'sneha.nair@example.com', '4321098765', '6th Avenue, Pune', 690),
            7: Customer(7, 'Karan Mehta', 'karan.mehta@example.com', '3210987654', '7th Circle, Kolkata', 740),
            8: Customer(8, 'Simran Kaur', 'simran.kaur@example.com', '2109876543', '8th Block, Hyderabad', 710),
            9: Customer(9, 'Aditya Roy', 'aditya.roy@example.com', '1098765432', '9th Path, Jaipur', 760),
            10: Customer(10, 'Pooja Gupta', 'pooja.gupta@example.com', '0987654321', '10th Lane, Chandigarh', 780)
        }
        self.next_loan_id = 1  # Initialize loan ID counter

    def get_customer_by_id(self, customer_id):
        return self.customers.get(customer_id)

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

    def get_customer_by_id(self, customer_id):
        # Replace this with actual customer retrieval logic
        return self.customers.get(customer_id)

    def calculate_interest(self, loan_id):
        loan = self.get_loan_by_id(loan_id)
        if loan:
            interest = (loan.principal_amount * loan.interest_rate * loan.loan_term) / 12
            return interest
        else:
            raise InvalidLoanException(f"Loan with ID {loan_id} not found.")

    def check_and_update_loan_status(self, loan_id):
        loan = self.get_loan_by_id(loan_id)
        if loan:
            if loan.customer.credit_score > 650:
                loan.loan_status = "Approved"
            else:
                loan.loan_status = "Rejected"
            print(f"Loan status for ID {loan_id}: {loan.loan_status}")
        else:
            raise InvalidLoanException(f"Loan with ID {loan_id} not found.")

    def get_loan_status(self, loan_id):
        loan = self.get_loan_by_id(loan_id)
        if loan:
            return loan.loan_status
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
