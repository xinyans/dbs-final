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

	def listVolumeCrash(self):
		cursor = self.conn.cursor()
		query = """
		SELECT Car_crash.municipality,Car_crash.year,
		count(Car_crash.crash_descriptor) as crash_count,
		SUM(Location_volumn.volume_count) as volume,
		FROM Location_volume NATURAL JOIN Car_crash
		GROUP BY municipality,year
		"""
		cursor.execute(query)
		records=cursor.fetchall()
		return records

	# User selects from the following: ramp, bridge, railroad crossing, and one-way.
	# Function returns how these affect crash rate
	def structureCrashRelation(self, structure_name):
		pass

	# User inputs a municipality name, case insensitive. If this municipality is not found, return empty.
	# Else return Crashes, Volume and crash rate of every year.
	def crashRateMunicipality(self, municipality_name):
		pass




