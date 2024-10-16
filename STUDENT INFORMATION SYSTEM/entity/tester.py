import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from entity.enrollment import Enrollment
from entity.payment import Payment
from entity.sis import SIS

def main():
    sis = SIS()

    student1 = Student(1, 'John', 'Doe', '1995-08-15', 'john.doe@example.com', '1234567890')
    student2 = Student(2, 'Jane', 'Smith', '1996-09-25', 'jane.smith@example.com', '0987654321')

    course1 = Course(1, 'Mathematics', 'MATH101', 'Dr. Alice')
    course2 = Course(2, 'Physics', 'PHYS101', 'Dr. Bob')

    sis.students.append(student1)
    sis.students.append(student2)
    sis.courses.append(course1)
    sis.courses.append(course2)

    sis.enroll_student_in_course(student1, course1)
    sis.enroll_student_in_course(student2, course2)
    
    print()

    sis.record_payment(student1, 5000.00, '2024-01-20')
    sis.record_payment(student2, 6000.00, '2024-02-15')

    print()
    sis.generate_enrollment_report(course2)
    print()

    sis.generate_payment_report(student1)

    num_enrollments, total_payments = sis.calculate_course_statistics(course1)
    print(f'\nStatistics for {course1.course_name}:')
    print(f'Number of Enrollments: {num_enrollments}, Total Payments: {total_payments}')

if __name__ == '__main__':
    main()
