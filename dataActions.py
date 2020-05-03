import psycopg2
from tabulate import tabulate

class DataActions:
    def __init__(self, params):
        self.host = params["host"] if "host" in params else "localhost"
        self.username = params["username"] if "username" in params else "postgres"
        if "database" in params:
            self.database = params["database"]
        else:
            raise ValueError("No database given.")
        if "password" in params:
            self.password = params["password"]
        else:
            raise ValueError("No password given.")
        connection_string = f"host='{self.host}' dbname='{self.database}' user='{self.user}' password='{self.password}'"
        self.connection = psycopg2.connect(connection_string)

    def importCsv(self, directory):
        pass

    def query(self, table, criterion):
        course_query = f"SELECT * FROM '{table}'"

