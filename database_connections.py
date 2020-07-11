import pyodbc
import runfile






def __init__(self, server, database, username, password, connections, cursor):
self.server = server
self.database = database
self.username = username
self.password = password
self.connections = connections
self.cursor = cursor

connections = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursor = connections.cursor()
    def conditions(self):
        try:
            with pyodbc.connect(connections, timeout=5) as connection:
                print("Connection established")
        except:
            print("Connection Timed out")
        else:
            return connection
    # next, we need to acquire the cursor from a connection - execute the code through the cursor. Fetch-iterate through the results by using the row objects that are returned by the cursor.fetch command
    # create a cursor from the connection

        print(connection)
        print(cursor)


query_result = cursor.execute('SELECT * FROM Products')
print("Printing query_result object",query_result)
# this is the command that allows us to fetch one row from the results
rows=query_result.fetchone()

# fetchmany() allows us to fetch more than one row
# fetchall()  is the command for all rows
print(type(rows)) # pyodbc.row object
print(rows[1])
print(rows.ProductName) # returns the same thing as the [1] index as Pname is in the 1st index column

rows = query_result.fetchmany(30)
for row in rows:
    print(row[0])

rows = query_result.fetchall()
for row in rows:
    print(row)
