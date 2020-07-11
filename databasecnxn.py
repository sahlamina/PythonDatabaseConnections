import pyodbc
# I put my credentials here below my class because it becomes available to everything in the class
class OpenConnection:
    # Database Login credentials
    server = "databases2.spartaglobal.academy"  # Server name
    database = "Northwind"  # Database name
    username = "SA"  # username
    password = "Passw0rd2018"

# here I am trying to establish a connection using the variables above
    def credentials(self):
        connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + self.server + ";DATABASE=" + self.database + \
                           ";UID=" + self.username + ";PWD=" + self.password
        try:
            with pyodbc.connect(connectionString, timeout=5) as connection:
                print("Connection established")
        except:
            print("Connection Timed out")
        else:
            cursor = connection.cursor()
            return cursor



















    # def fetch_queries(self):
    #     #  here we called the overall class to try and link the method above to this queries method
    #     obj = OpenConnection()
    #     # this serves as a link between my credentials method and my queries method. Without it, i would have no access to my cursor variable
    #     cursor = obj.credentials()
    #
    #     query_result = cursor.execute('SELECT * FROM Products')
    #     print("Printing query_result object:",query_result)
    #     rows = query_result.fetchone()
    #     print(type(rows))
    #     print(rows[1])
    #     print(rows.ProductName)






            # print("-------------FETCHMANY--------------------")
            # rows=query_result.fetchmany(30)
            # for row in rows:
            #     print(row.ProductID)
            #
            # print("-------------FETCHALL--------------------")
            # rows=query_result.fetchall()
            # for row in rows:
            #     print("ProductName::"+row.ProductName, "Costs :",row.UnitPrice)


