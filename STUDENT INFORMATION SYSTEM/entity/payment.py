class Payment:
    def __init__(self, payment_id, student_id, amount, payment_date):
        self.payment_id = payment_id
        self.student = None; # Store reference to Student object 
        self.student_id = student_id  # Store student ID
        self.amount = amount
        self.payment_date = payment_date

    def get_student(self):
        return self.student  # Return the Student object
    
    def set_student(self, student):
        self.student = student  # Method to set the Student referen

    def get_student_id(self):
        return self.student_id  # Return the Student ID

    def get_payment_amount(self):
        return self.amount  # Return the payment amount

    def get_payment_date(self):
        return self.payment_date  # Return the payment date

    def display_payment_info(self):
        print(f"Payment ID: {self.payment_id}")
        print(f"Student ID: {self.student_id} (Name: {self.student.first_name} {self.student.last_name})")
        print(f"Amount: {self.amount}")
        print(f"Payment Date: {self.payment_date}")
