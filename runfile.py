from queries import *

class Interface(Queries):

    call = Queries()
    call.fetch_queries()

    # Is it necessary to inherit queries in this class? The inheritance may be redundant as you have already imported *
    # consider your exceptions