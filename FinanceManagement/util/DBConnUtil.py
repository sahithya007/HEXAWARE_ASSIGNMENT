import pyodbc
import sys
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(base_dir)

from util.DBPropertyUtil import get_property_string

class DBConnUtil:
    connection=None

    @staticmethod
    def get_connection():
        if DBConnUtil.connection is None:
            connection_string=get_property_string()
            print(f"Connection String: {connection_string}")  
            try:
                DBConnUtil.connection = pyodbc.connect(connection_string)
                print("Connected Successfully")
            except Exception as e:
                print("Connection failed:", e)
        return DBConnUtil.connection

