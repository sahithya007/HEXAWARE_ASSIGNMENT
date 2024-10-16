from abc import ABC, abstractmethod

class SISServiceProvider(ABC):
    
    @abstractmethod
    def add_enrollment(self, student, course, enrollment_date):
        pass
    
    @abstractmethod
    def assign_course_to_teacher(self, course, teacher):
        pass
    
    @abstractmethod
    def add_payment(self, student, amount, payment_date):
        pass
    
    @abstractmethod
    def generate_enrollment_report_for_course(self, course_id):
        pass
    
    @abstractmethod
    def generate_payment_report_for_student(self, student_id):
        pass
    
    @abstractmethod
    def calculate_course_statistics(self, course):
        pass
