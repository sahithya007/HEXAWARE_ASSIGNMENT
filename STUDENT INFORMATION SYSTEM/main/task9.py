import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)
import pyodbc
from util.db_conn_util import DBConnUtil
from util.DatabaseManager import DatabaseManager


if __name__ == "__main__":
    db_manager = DatabaseManager()


    first_name = 'Sarah'
    last_name = 'Smith'
    email = 'sarah.smith@example.com'

    db_manager.insert_teacher(first_name, last_name, email)

    course_id = 12


    query = "SELECT * FROM Courses WHERE course_id = ?"
    course = db_manager.execute_query(query, (course_id,))

    if course:
        teacher = db_manager.get_teacher_by_email(email)

        if teacher:
           
            update_query = "UPDATE Courses SET teacher_id = ? WHERE course_id = ?"
            db_manager.execute_query(update_query, (teacher[0], course_id))
            print(f"Assigned {first_name} {last_name} to teach course ID {course_id}.")
        else:
            print("Teacher not found.")
    else:
        print("Course not found.")

    db_manager.close()