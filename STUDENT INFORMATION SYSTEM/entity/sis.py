import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from util.DatabaseManager import DatabaseManager
from entity.enrollment import Enrollment
from entity.payment import Payment
from entity.student import Student

class SIS:
    def __init__(self):
        self.students = []
        self.courses = []
        self.enrollments = []
        self.payments = []
        self.teachers = []
        self.database_manager = DatabaseManager()  # Initialize DatabaseManager here
        
    def add_enrollment(self, student, course, enrollment_date):
        if any(enrollment.student_id == student.student_id and enrollment.course_id == course.course_id for enrollment in self.enrollments):
            raise Exception("Student is already enrolled in this course.")
        
        enrollment = Enrollment(len(self.enrollments) + 1, student.student_id, course.course_id, enrollment_date)
        
        enrollment.set_student(student)
        enrollment.set_course(course)

        self.enrollments.append(enrollment)
 
        student.enrolled_courses.append(course)
        course.enrollments.append(enrollment)
        
        print(f'Enrolled {student.first_name} in {course.course_name} on {enrollment_date}')
        
    def assign_course_to_teacher(self, course, teacher):
        if course not in teacher.assigned_courses:
            teacher.assigned_courses.append(course)
            print(f'Course {course.course_name} has been assigned to teacher {teacher.first_name} {teacher.last_name}.')
        else:
            print(f'Course {course.course_name} is already assigned to teacher {teacher.first_name} {teacher.last_name}.')

    def add_payment(self, student, amount, payment_date):
        payment = Payment(len(self.payments) + 1, student.student_id, amount, payment_date)
        
        student.make_payment(amount, payment_date)
        
        self.payments.append(payment)
        
        print(f'Recorded payment of {amount} from {student.first_name} on {payment_date}')
    
    def get_enrollments_for_student(self, student):
        """Retrieve all enrollments for a specific student."""
        return [enrollment for enrollment in self.enrollments if enrollment.student.student_id == student.student_id]  
        
    def get_courses_for_teacher(self, teacher):
        """Retrieve all courses assigned to a specific teacher."""
        return [course for course in self.courses if course in teacher.assigned_courses]

    def enroll_student_in_course(self, student, course):
        enrollment_date = '2024-01-01'  # Static date for demonstration
        enrollment = Enrollment(len(self.enrollments) + 1, student.student_id, course.course_id, enrollment_date)
        self.enrollments.append(enrollment)
        print(f'Enrolled {student.first_name} in {course.course_name} on {enrollment_date}')
        
    def record_payment(self, student, amount, payment_date):
        payment = Payment(len(self.payments) + 1, student.student_id, amount, payment_date)
        self.payments.append(payment)
        print(f'Recorded payment of {amount} from {student.first_name} on {payment_date}')

    def generate_enrollment_report(self, course):
        enrollments = [enrollment for enrollment in self.enrollments if enrollment.course_id == course.course_id]
        
        # Check if there are enrollments
        if not enrollments:
            print(f"\nNo enrollments found for {course.course_name}")
            return enrollments  # Return empty list instead of None

        print(f'\nEnrollment Report for {course.course_name}:')
        for enrollment in enrollments:
            print(f'Student ID: {enrollment.student_id}, Course ID: {enrollment.course_id}, Enrollment Date: {enrollment.enrollment_date}')

        return enrollments  # Return the list of enrollments

    def generate_payment_report(self, student):
        payment_report = [payment for payment in self.payments if payment.student_id == student.student_id]
        print(f'\nPayment Report for {student.first_name} {student.last_name}:')
        for payment in payment_report:
            print(f'Amount: {payment.amount}, Payment Date: {payment.payment_date}')

    def calculate_course_statistics(self, course):
        enrollments = [enrollment for enrollment in self.enrollments if enrollment.course_id == course.course_id]
        if not enrollments:
            print(f"\nNo enrollments found for {course.course_name}")
            return 0, 0  # Return 0 for both enrollments and total payments if none
        total_payments = sum(payment.amount for payment in self.payments if payment.student_id in [e.student_id for e in enrollments])
        return len(enrollments), total_payments
    
    def generate_enrollment_report_for_course(self, course_id):
        course = self.database_manager.get_course_by_id(course_id)  # Use the database_manager instance
        
        if not course:
            print(f"Course with ID '{course_id}' not found.")
            return

        enrollments = self.database_manager.get_enrollments_by_course(course_id)  # Use the database_manager instance
        
        if not enrollments:
            print(f"No enrollments found for course ID '{course_id}'.")
            return

        print(f"\nEnrollment Report for Course ID '{course_id}':")
        print("---------------------------------------------------")
        for enrollment in enrollments:
            student_id, first_name, last_name, enrollment_date = enrollment
            print(f"Student ID: {student_id}, Name: {first_name} {last_name}, Enrollment Date: {enrollment_date}")
        print("---------------------------------------------------")
