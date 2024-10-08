class Loan:
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, loan_type, loan_status="Pending"):
        self.loan_id = loan_id
        self.customer = customer
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status

    def __str__(self):
        return f"Loan ID: {self.loan_id}, Customer: {self.customer.name}, Status: {self.loan_status}"
