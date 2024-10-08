
import sys
sys.path.append(r"C:\Users\SAHITHYA\OneDrive\Desktop\LOAN MANAGEMENT SYSTEM")
from entity.Loan import Loan
class HomeLoan(Loan):
    def __init__(self, loan_id=None, customer=None, principal_amount=None, interest_rate=None, loan_term=None, property_address=None, property_value=None, loan_status="Pending"):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "HomeLoan", loan_status)
        self.property_address = property_address
        self.property_value = property_value

    def __str__(self):
        return super().__str__() + f", Property Address: {self.property_address}, Property Value: {self.property_value}"

    # Getters and Setters
    def get_property_address(self):
        return self.property_address

    def set_property_address(self, property_address):
        self.property_address = property_address

    def get_property_value(self):
        return self.property_value

    def set_property_value(self, property_value):
        self.property_value = property_value
