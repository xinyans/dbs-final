import psycopg2
import psycopg2.extras

class Vehicles_data:
	def __init__(self, connection_string):
		self.conn = psycopg2.connect(connection_string)

	def listTrafficVolume(self,volume):
		cursor = self.conn.cursor()
		query = """
		SELECT municipality,year FROM Location_volume 
		GROUP BY municipality,year HAVING SUM(volume_count) >= %s
		"""
		cursor.execute(query,(volume,))
		records=cursor.fetchall()
		return records
