import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
from util.db_conn_util import DBConnUtil

class DatabaseManager:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        if self.conn:
            self.cursor = self.conn.cursor()
    
    def close(self):
        if self.conn:
            self.conn.close()

    def begin_transaction(self):
        self.conn.autocommit = False

    def commit_transaction(self):
        self.conn.commit()
        self.conn.autocommit = True

    def rollback_transaction(self):
        self.conn.rollback()
        self.conn.autocommit = True

    def insert_student(self, first_name, last_name, date_of_birth, email, phone_number):
        try:
            self.cursor.execute(
                "INSERT INTO Students (first_name, last_name, date_of_birth, email, phone_number) VALUES (?, ?, ?, ?, ?)",
                (first_name, last_name, date_of_birth, email, phone_number)
            )
            self.conn.commit()
            print(f"Inserted student: {first_name} {last_name}")
        except Exception as e:
            print("Error inserting student:", e)

    def update_student(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        try:
            self.cursor.execute(
                "UPDATE Students SET first_name = ?, last_name = ?, date_of_birth = ?, email = ?, phone_number = ? WHERE student_id = ?",
                (first_name, last_name, date_of_birth, email, phone_number, student_id)
            )
            self.conn.commit()
            print(f"Updated student ID {student_id}")
        except Exception as e:
            print("Error updating student:", e)

    def insert_enrollment(self, student_id, course_id, enrollment_date):
        try:
            self.cursor.execute(
                "INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)",
                (student_id, course_id, enrollment_date)
            )
            self.conn.commit()
            print(f"Inserted enrollment for student ID {student_id} in course ID {course_id}")
        except Exception as e:
            print("Error inserting enrollment:", e)

    def record_payment(self, student_id, amount, payment_date):
        try:
            self.cursor.execute(
                "INSERT INTO Payments (student_id, amount, payment_date) VALUES (?, ?, ?)",
                (student_id, amount, payment_date)
            )
            self.conn.commit()
            print(f"Inserted payment of {amount} from student ID {student_id}")
        except Exception as e:
            print("Error inserting payment:", e)

    def enroll_student_with_payment(self, student_id, course_id, enrollment_date, amount, payment_date):
        self.begin_transaction()
        try:
            self.insert_enrollment(student_id, course_id, enrollment_date)
            self.record_payment(student_id, amount, payment_date)
            self.commit_transaction()
        except Exception as e:
            self.rollback_transaction()
            print("Transaction failed:", e)
            
    def insert_teacher(self, first_name, last_name, email):
        try:
            # Check if the teacher already exists
            existing_teacher = self.get_teacher_by_email(email)
            if existing_teacher:
                print(f"Teacher with email {email} already exists.")
                return
            
            self.cursor.execute(
                "INSERT INTO Teacher (first_name, last_name, email) VALUES (?, ?, ?)",
                (first_name, last_name, email)
            )
            self.conn.commit()
            print(f"Inserted teacher: {first_name} {last_name}")
        except Exception as e:
            print("Error inserting teacher:", e)

    def update_course_teacher(self, course_code, teacher_id):
        try:
            self.cursor.execute(
                "UPDATE Courses SET teacher_id = ? WHERE course_code = ?",
                (teacher_id, course_code)
            )
            self.conn.commit()
            print(f"Assigned teacher ID {teacher_id} to course code {course_code}")
        except Exception as e:
            print("Error updating course teacher:", e)

    def get_course_by_code(self, course_code):
        try:
            course = self.cursor.execute(
                "SELECT course_id FROM Courses WHERE course_code = ?",
                (course_code,)
            ).fetchone()
            return course
        except Exception as e:
            print("Error fetching course:", e)
            return None

    def get_teacher_by_email(self, email):
        try:
            teacher = self.cursor.execute(
                "SELECT teacher_id FROM Teacher WHERE email = ?",
                (email,)
            ).fetchone()
            return teacher
        except Exception as e:
            print("Error fetching teacher:", e)
            return None

    def dynamic_query(self, table, columns=None, conditions=None, order_by=None):
        try:
            columns = ', '.join(columns) if columns else '*'
            query = f"SELECT {columns} FROM {table}"
            if conditions:
                query += " WHERE " + ' AND '.join(conditions)
            if order_by:
                query += " ORDER BY " + order_by
            
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print("Error executing dynamic query:", e)
            return []
        
    def execute_query(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            if query.strip().upper().startswith("SELECT"):
                return self.cursor.fetchall()
            else:
                self.conn.commit()
                return None
        except Exception as e:
            print("Error executing query:", e)
            return None


    def get_students(self):
        return self.dynamic_query("Students")

    def get_courses(self):
        return self.dynamic_query("Courses")

    def get_enrollments(self):
        return self.dynamic_query("Enrollments")

    def get_teachers(self):
        return self.dynamic_query("Teacher")

    def get_payments(self):
        return self.dynamic_query("Payments")
    
    def get_enrollments_by_course(self, course_id):
        try:
            enrollments = self.cursor.execute(
                "SELECT e.student_id, s.first_name, s.last_name, e.enrollment_date "
                "FROM Enrollments e "
                "JOIN Students s ON e.student_id = s.student_id "
                "WHERE e.course_id = ?",
                (course_id,)
            ).fetchall()
            return enrollments
        except Exception as e:
            print("Error fetching enrollments:", e)
            return []
        
    def get_course_by_id(self, course_id):
        try:
            course = self.cursor.execute(
                "SELECT course_id, course_name FROM Courses WHERE course_id = ?",
                (course_id,)
            ).fetchone()
            return course
        except Exception as e:
            print("Error fetching course:", e)
            return None
