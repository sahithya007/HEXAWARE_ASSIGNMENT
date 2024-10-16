class Enrollment:
    def __init__(self, enrollment_id, student, course, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student_id = None
        self.course_id = None
        self.enrollment_date = enrollment_date
        self.student = student # To hold reference to Student object
        self.course = course   # To hold reference to Course object

    def set_student(self, student):
        self.student = student  # Method to set the Student reference

    def get_student(self):
        return self.student  # Method to get the Student object

    def set_course(self, course):
        self.course = course  # Method to set the Course reference

    def get_course(self):
        return self.course  # Method to get the Course object

    def display_enrollment_info(self):
        student_name = f"{self.student.first_name} {self.student.last_name}" if self.student else "N/A"
        course_name = self.course.course_name if self.course else "N/A"
        
        print(f"Enrollment ID: {self.enrollment_id}")
        print(f"Student Name: = (Name: {student_name})")
        print(f"Course Name:(Course Name: {course_name})")
        print(f"Enrollment Date: {self.enrollment_date}")
