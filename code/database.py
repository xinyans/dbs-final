import psycopg2
import psycopg2.extras

class Vehicles_data:
	def __init__(self, connection_string):
		self.conn = psycopg2.connect(connection_string)

	def listTrafficVolume(self,volume):
		'''
		Lists the municipality and the year that have a traffic volume greater or
		equal than the specified volume.
		'''

		cursor = self.conn.cursor()
		query = """
		SELECT municipality,year FROM Location_volume 
		GROUP BY municipality,year HAVING SUM(volume_count) >= %s
		"""
		cursor.execute(query,(volume,))
		records=cursor.fetchall()
		return records

		
	def listVolumeCrash(self):
		'''
		Lists the number of crashes in a specific year and municipality.
		'''

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
		cursor = self.conn.cursor()
		query = """
				SELECT SUM(c.crash_sum) AS crash_total, SUM(c.volume_sum) AS volume_total, SUM(c.crash_sum)/SUM(c.volume_sum)*100 AS percentage, structure FROM
					(SELECT a.municipality, a.county, structure, SUM(crash_count) AS crash_sum, SUM(a.vol) AS volume_sum FROM 
						(SELECT year, municipality, county, %s AS structure, SUM(volume_count) AS vol FROM
						Location_volume GROUP BY (year, municipality, county, %s)) a
					JOIN
						(SELECT year, municipality, county, COUNT(incident_date) AS crash_count FROM Car_crash GROUP BY (year, municipality, county)) b
					ON a.year=b.year and LOWER(a.municipality)=LOWER(b.municipality) and LOWER(a.county)=LOWER(b.county)
					WHERE vol IS NOT NULL
					GROUP BY (a.year, a.municipality, a.county, structure)) c
				GROUP BY structure;
				"""
		cursor.execute(query, (structure_name, structure_name,))
		records = cursor.fetchall()
		return records

	# User inputs a municipality name, case insensitive. If this municipality is not found, return empty.
	# Else return Crashes, Volume and crash rate of every year.
	def crashRateMunicipality(self, municipality_name):
		pass




