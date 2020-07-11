from databasecnxn import OpenConnection



class Queries:

    def fetch_queries(self):
        #  here we called the overall class to try and link the method above to this queries method
        obj = OpenConnection()
        # this serves as a link between my credentials method and my queries method. Without it, i would have no access to my cursor variable
        cursor = obj.credentials()

        query_result = cursor.execute("SELECT AVG(UnitPrice) FROM Products")
        print("The average unit price is: ")
        rows = query_result.fetchone()
        print(rows)
