import sys
sys.path.append(r"C:\Users\SAHITHYA\OneDrive\Desktop\LOAN MANAGEMENT SYSTEM")
from entity.Loan import Loan

class CarLoan(Loan):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, car_model, car_value, loan_status="Pending"):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "CarLoan", loan_status)
        self.car_model = car_model
        self.car_value = car_value

    def __str__(self):
        return super().__str__() + f", Car Model: {self.car_model}, Car Value: {self.car_value}"
