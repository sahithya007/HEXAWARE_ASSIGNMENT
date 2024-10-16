from util.DatabaseManager import DatabaseManager
from entity.enrollment import Enrollment
from entity.payment import Payment

class SISDatabaseServiceProvider(SISServiceProvider):
    
    def __init__(self):
        self.database_manager = DatabaseManager()  # Initialize DatabaseManager for DB interactions
    
    def add_enrollment(self, student, course, enrollment_date):
        enrollment = Enrollment(len(self.database_manager.get_all_enrollments()) + 1, student.student_id, course.course_id, enrollment_date)
        self.database_manager.save_enrollment(enrollment)
        print(f"Enrolled {student.first_name} in {course.course_name} on {enrollment_date}")
    
    def assign_course_to_teacher(self, course, teacher):
        self.database_manager.assign_course_to_teacher(course, teacher)
        print(f"Assigned course {course.course_name} to teacher {teacher.first_name} {teacher.last_name}.")
    
    def add_payment(self, student, amount, payment_date):
        payment = Payment(len(self.database_manager.get_all_payments()) + 1, student.student_id, amount, payment_date)
        self.database_manager.save_payment(payment)
        print(f"Recorded payment of {amount} from {student.first_name} on {payment_date}")
    
    def generate_enrollment_report_for_course(self, course_id):
        course = self.database_manager.get_course_by_id(course_id)
        if not course:
            print(f"Course with ID '{course_id}' not found.")
            return

        enrollments = self.database_manager.get_enrollments_by_course(course_id)
        if not enrollments:
            print(f"No enrollments found for course ID '{course_id}'.")
            return

        print(f"\nEnrollment Report for Course ID '{course_id}':")
        for enrollment in enrollments:
            student_id, first_name, last_name, enrollment_date = enrollment
            print(f"Student ID: {student_id}, Name: {first_name} {last_name}, Enrollment Date: {enrollment_date}")

    def generate_payment_report_for_student(self, student_id):
        payments = self.database_manager.get_payments_by_student_id(student_id)
        if not payments:
            print(f"No payments found for student ID '{student_id}'.")
            return

        print(f"\nPayment Report for Student ID '{student_id}':")
        for payment in payments:
            print(f"Amount: {payment.amount}, Payment Date: {payment.payment_date}")
    
    def calculate_course_statistics(self, course):
        enrollments = self.database_manager.get_enrollments_by_course(course.course_id)
        if not enrollments:
            print(f"No enrollments found for {course.course_name}")
            return 0, 0

        total_payments = sum(payment.amount for payment in self.database_manager.get_all_payments()
                             if payment.student_id in [e.student_id for e in enrollments])
        return len(enrollments), total_payments
