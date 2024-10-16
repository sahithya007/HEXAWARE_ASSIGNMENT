# main/task11.py

import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from entity.sis import SIS

if __name__ == "__main__":
    sis = SIS()
    course_id = 101 # Set the course name to match what was added
    sis.generate_enrollment_report_for_course(course_id)
