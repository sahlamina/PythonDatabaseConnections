# Write import pyodbc
import pyodbc  # pyobdc module used to connect to microsoft database(s)
import re  # importing Regular expression block

# Got to Python
# Here we are going to establish a connection and read data from the database in the python console

# This allows us to showcase data from a database in real-time which we would display to the front-end, E.G.
# the UI interface for users. As they will NEVER have access directly to the database or its data.

# 1) DB Server connection variables
# Goal -> Establish a connection with the database
# ODBC -> is a connection to a microsoft database


# from database_OOP import database_OOP

# Connection credentials
server = "databases2.spartaglobal.academy"  # Server name
database = "Northwind"  # Database name
# Database Login credentials
username = "SA"  # username
password = "Passw0rd2018"  # password

# OOP Part
# data_oop = database_OOP(server,database,username,password)
# oop_connection = data_oop.establish_connection()
# data_oop.execute_sql('SELECT * FROM Products', oop_connection)

# connection = DRIVER_USED, SERVER = 'your_server', DATABASE = 'your_database',
#           USER = 'your_username', PWD = 'your_password'
connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server + ";DATABASE=" + database + \
                   ";UID=" + username + ";PWD=" + password

# Try to connect to the database, if it hasn't connected within the timeout time (5 seconds) then the request has timed
# out and an exception will be raised.
try:
    with pyodbc.connect(connectionString, timeout=5) as connection:
        print("Connection did not time out")
except (ConnectionError, pyodbc.OperationalError, pyodbc.DatabaseError):
    print("Connection has timed out")
except pyodbc.InterfaceError:
    print("Invalid connection to DB interface")
else:
    # This is just me experimenting with connecting and querying database
    cursor = connection.cursor()  # The cursor is a control structure
    # This allows us to control and manage rows of data from a response. In the pyodbc, instance is used to manage
    # our queries directly with the database
    cursor.execute("SELECT * FROM customers")  # execute query using connection/ cursor
    rows = cursor.fetchall()
    for row in rows:
        if row.Country == "UK" and re.search("Sales.+", row.ContactTitle):
            print(row)

