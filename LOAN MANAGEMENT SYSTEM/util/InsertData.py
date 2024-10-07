import sys
sys.path.append(r"C:\Users\SAHITHYA\OneDrive\Desktop\LOAN MANAGEMENT SYSTEM")
import pyodbc
from util.DBUtil import DBUtil

def insert_data():
    conn = DBUtil.getDBConn()
    if conn:
        try:
            cursor = conn.cursor()

            # Insert data into Customers table (omit CustomerID)
            customers = [
                ('John Doe', 'john.doe@example.com', '1234567890', '123 Main St', 720),
                ('Jane Smith', 'jane.smith@example.com', '0987654321', '456 Oak St', 680),
                ('Mike Johnson', 'mike.j@example.com', '2345678901', '789 Pine St', 750),
                ('Emily Davis', 'emily.d@example.com', '3456789012', '101 Maple St', 800),
                ('Sarah Lee', 'sarah.lee@example.com', '4567890123', '202 Birch St', 660),
                ('David Brown', 'david.b@example.com', '5678901234', '303 Cedar St', 690),
                ('Laura White', 'laura.w@example.com', '6789012345', '404 Cherry St', 740),
                ('Tom Green', 'tom.g@example.com', '7890123456', '505 Spruce St', 710),
                ('Rachel Adams', 'rachel.a@example.com', '8901234567', '606 Willow St', 760),
                ('Steve Black', 'steve.b@example.com', '9012345678', '707 Ash St', 780)
            ]

            cursor.executemany("""
                INSERT INTO Customers (Name, Email, Phone, Address, CreditScore) 
                VALUES (?, ?, ?, ?, ?)
            """, customers)

            print(f"{cursor.rowcount} records inserted successfully into Customers table.")

            # Insert data into Loans table (you can keep LoanID if it's not an identity column)
            loans = [
                (1, 500000, 5.5, 60, 'HomeLoan', 'Pending'),
                (2, 300000, 4.2, 48, 'CarLoan', 'Approved'),
                (3, 700000, 6.0, 72, 'HomeLoan', 'Pending'),
                (4, 150000, 3.8, 36, 'CarLoan', 'Approved'),
                (5, 250000, 4.9, 60, 'CarLoan', 'Pending'),
                (6, 800000, 5.7, 120, 'HomeLoan', 'Approved'),
                (7, 600000, 6.2, 84, 'HomeLoan', 'Pending'),
                (8, 350000, 4.5, 72, 'CarLoan', 'Approved'),
                (9, 450000, 5.0, 60, 'HomeLoan', 'Pending'),
                (10, 500000, 5.3, 48, 'CarLoan', 'Approved')
            ]

            cursor.executemany("""
                INSERT INTO Loans (CustomerID, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, loans)

            print(f"{cursor.rowcount} records inserted successfully into Loans table.")

            # Insert data into HomeLoans table
            home_loans = [
                (1, '123 Main St', 500000),
                (2, '789 Pine St', 700000),
                (3, '456 Oak St', 300000),
                (4, '101 Maple St', 800000),
                (5, '404 Cherry St', 600000),
                (6, '606 Willow St', 450000),
                (7, '202 Birch St', 250000),
                (8, '505 Spruce St', 350000),
                (9, '707 Ash St', 500000),
                (10, '303 Cedar St', 690000)
            ]

            cursor.executemany("""
                INSERT INTO HomeLoans (LoanID, PropertyAddress, PropertyValue) 
                VALUES (?, ?, ?)
            """, home_loans)

            print(f"{cursor.rowcount} records inserted successfully into HomeLoans table.")

            # Insert data into CarLoans table
            car_loans = [
                (1, 'Toyota Camry', 30000),
                (2, 'Honda Civic', 25000),
                (3, 'Ford Mustang', 50000),
                (4, 'Tesla Model 3', 40000),
                (5, 'BMW X5', 55000),
                (6, 'Audi A6', 60000),
                (7, 'Mercedes-Benz C-Class', 45000),
                (8, 'Lexus RX', 50000),
                (9, 'Hyundai Sonata', 28000),
                (10, 'Chevrolet Malibu', 35000)
            ]

            cursor.executemany("""
                INSERT INTO CarLoans (LoanID, CarModel, CarValue) 
                VALUES (?, ?, ?)
            """, car_loans)

            print(f"{cursor.rowcount} records inserted successfully into CarLoans table.")

            # Close the cursor
            cursor.close()
        except Exception as e:
            print("Error inserting records:", e)
        finally:
            conn.close()

# Call insert_data() to execute
if __name__ == "__main__":
    insert_data()
