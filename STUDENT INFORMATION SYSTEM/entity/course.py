import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)


from entity.enrollment import Enrollment

class Course:
    def __init__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.enrollments = []  # List to store Enrollment objects
        self.teacher = None     # To hold the assigned teacher

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def update_course_info(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor_name = instructor

    def display_course_info(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor Name: {self.instructor_name}")

    def enroll_student(self, student, enrollment_date):
        enrollment = Enrollment(len(self.enrollments) + 1, student.student_id, self.course_id, enrollment_date)
        self.enrollments.append(enrollment)

    def get_enrollments(self):
        return self.enrollments

    def get_teacher(self):
        return self.teacher