class Customer:
    def __init__(self, customer_id, name, email, phone, address, credit_score):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.credit_score = credit_score

    def __str__(self):
        return f"Customer: {self.name}, Credit Score: {self.credit_score}"
