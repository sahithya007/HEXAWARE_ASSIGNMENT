import sys
import os
from decimal import Decimal

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from util.DatabaseManager import DatabaseManager

db_manager = DatabaseManager()

first_name = 'Jane'
last_name = 'Smith'

try:
    query = "SELECT student_id, outstanding_balance FROM Students WHERE first_name = ? AND last_name = ?"
    student = db_manager.execute_query(query, (first_name, last_name))

    if student:
        student_id = student[0][0]
        outstanding_balance = student[0][1] if student[0][1] is not None else Decimal('0.00')
        print(f"Found student ID {student_id} with outstanding balance {outstanding_balance}")

        payment_amount = Decimal('500.00')
        payment_date = '2023-04-10'

        if outstanding_balance > Decimal('0.00'):
            db_manager.record_payment(student_id, payment_amount, payment_date)
            print(f"Recorded payment of {payment_amount} for student ID {student_id} on {payment_date}")

            # Update the student's balance
            new_balance = outstanding_balance - payment_amount
            if new_balance < Decimal('0.00'):
                new_balance = Decimal('0.00')

            update_balance_query = "UPDATE Students SET outstanding_balance = ? WHERE student_id = ?"
            db_manager.execute_query(update_balance_query, (new_balance, student_id))
            print(f"Updated outstanding balance to {new_balance} for student ID {student_id}")
        else:
            print("Payment not required, outstanding balance is already 0 or negative.")
    else:
        print("Student not found.")
except Exception as e:
    print("Error processing payment:", e)
finally:
    db_manager.close()
