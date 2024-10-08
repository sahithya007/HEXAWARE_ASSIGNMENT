import pyodbc

class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            # Define the connection string
            conn = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=sahithya;'
                'Database=LoanManagementSystem;'
                'Trusted_Connection=yes;'
            )
            print("Connected Successfully to the database.")
            return conn  # Return the connection object
        except pyodbc.Error as e:
            print("Connection failed with error:", e)
            return None  # Return None if connection fails
