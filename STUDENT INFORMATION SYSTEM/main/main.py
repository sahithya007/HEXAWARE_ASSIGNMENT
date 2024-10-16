# main/main.py

import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from entity.sis import SIS
from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from entity.payment import Payment

def main():
    # Initialize the SIS system
    sis = SIS()

    # Create some sample students
    student1 = Student(1, 'John', 'Doe', '1995-08-15', 'john.doe@example.com', '1234567890')
    student2 = Student(2, 'Jane', 'Smith', '1996-09-25', 'jane.smith@example.com', '0987654321')

    # Create some sample courses
    course1 = Course(1, 'Introduction to Programming', 'CS101', 'Dr. Alice')
    course2 = Course(2, 'Mathematics 101', 'MATH101', 'Dr. Bob')

    # Create some sample teachers
    teacher1 = Teacher(1, 'Alice', 'Johnson', 'alice.johnson@example.com')
    teacher2 = Teacher(2, 'Bob', 'Smith', 'bob.smith@example.com')

    # Add students, courses, and teachers to the SIS
    sis.students.append(student1)
    sis.students.append(student2)
    sis.courses.append(course1)
    sis.courses.append(course2)
    sis.teachers.append(teacher1)
    sis.teachers.append(teacher2)

    # Enroll students in courses
    sis.add_enrollment(student1, course1, '2024-01-01')
    sis.add_enrollment(student2, course2, '2024-01-01')

    # Assign courses to teachers
    sis.assign_course_to_teacher(course1, teacher1)
    sis.assign_course_to_teacher(course2, teacher2)

    # Record payments
    sis.add_payment(student1, 500, '2024-02-15')
    sis.add_payment(student2, 600, '2024-02-16')

    # Get enrollments for a student
    print(f"\nEnrollments for {student1.first_name} {student1.last_name}:")
    enrollments = sis.get_enrollments_for_student(student1)
    for enrollment in enrollments:
        print(f"Enrolled in {enrollment.course.course_name} on {enrollment.enrollment_date}")

    # Get courses for a teacher
    print(f"\nCourses assigned to {teacher1.first_name} {teacher1.last_name}:")
    courses = sis.get_courses_for_teacher(teacher1)
    for course in courses:
        print(course.course_name)

if __name__ == "__main__":
    main()
