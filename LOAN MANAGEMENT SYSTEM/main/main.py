def menu():
    print("--- Loan Management System ---")
    print("1. Apply for Loan")
    print("2. Get All Loans")
    print("3. Get Loan by ID")
    print("4. Loan Repayment")
    print("5. Calculate EMI")  # Ensure this option is included
    print("6. Exit")
    from util.InsertData import insert_data  # Adjust according to your file structure

def insert_data():
    # Your existing data insertion logic here
    pass  # Replace this with actual insertion code


def calculate_emi(loan_repository):
    loan_id = int(input("Enter Loan ID: "))
    try:
        emi = loan_repository.calculate_emi(loan_id)  # Call calculate_emi method from repository
        print(f"EMI for Loan ID {loan_id} is: {emi:.2f}")  # Display the EMI amount
    except InvalidLoanException as e:
        print(e)

def run(self):
    loan_repository = LoanRepositoryImpl()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            self.apply_loan(loan_repository)  # Apply for a loan
        elif choice == '2':
            loan_repository.get_all_loans()  # Get all loans
        elif choice == '3':
            self.get_loan_by_id()  # Get loan by ID
        elif choice == '4':
            self.loan_repayment()  # Call loan repayment method
        elif choice == '5':
            calculate_emi(loan_repository)  # Calculate EMI
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()
