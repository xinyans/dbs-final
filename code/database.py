import psycorg2
import psycorg2.extras
class Vehicles_data:
	def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)
    def __init__(self,volume):
    	cursor = self.conn.cursor
    	query = "SELECT municipality,year FROM Location_volume WHERE sum(count)>=%d \
    	group by municipality,year"
    	cursor.execute(query,(volume,))
    	records=cursor.fetchall()
    	return records
