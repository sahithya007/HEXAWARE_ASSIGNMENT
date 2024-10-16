# DBConnUtil.py
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        connection_string = DBPropertyUtil.get_connection_string()
        try:
            conn = pyodbc.connect(connection_string)
            print("Connected Successfully")
            return conn
        except Exception as e:
            print("Connection failed:", e)
            return None
