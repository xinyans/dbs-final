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
		SELECT municipality,year FROM volume NATURAL JOIN roads 
		WHERE municipality IS NOT NULL GROUP BY municipality, year 
		HAVING SUM(volume_count) >= %s
		"""
		cursor.execute(query,(volume,))
		records=cursor.fetchall()
		return records

	def vehicleAndCarCrash(self,vehicle_number):
		"""list the municipality,year and crash_descriptor of the car crashes 
		that have the number_of_vehicles involved equals or more than the number 
		users input ordered by the number_of_vehicles in descending order"""
		cursor = self.conn.cursor()
		query = """
		SELECT municipality, year,
		crash_descriptor
		FROM Car_crash
		WHERE number_of_vehicles>=%s
		ORDER BY number_of_vehicles desc
		"""
		cursor.execute(query,(vehicle_number,))
		records=cursor.fetchall()
		return records

	def listVolumeCrash(self):
		'''
		Lists the number of crashes and total traffic in a specific year and municipality.
		'''

		cursor = self.conn.cursor()
		query = """
		SELECT traffic.municipality, traffic.year, crashes.crash_count, 
		traffic.total_volume
		FROM (
			SELECT municipality, year, SUM(volume_count) as total_volume
			FROM Volume NATURAL JOIN Roads GROUP BY year, municipality
			HAVING SUM(volume_count) IS NOT NULL
		) traffic JOIN (
			SELECT municipality, year, COUNT(crash_descriptor) as crash_count
			FROM Car_crash GROUP BY year, municipality
		) crashes ON (
			traffic.municipality ILIKE crashes.municipality 
			AND traffic.year = crashes.year
		)
		where crashes.crash_count>100
		"""
		cursor.execute(query)
		records=cursor.fetchall()
		return records

	# User selects from the following: ramp, bridge, railroad crossing, and one-way. Any other input is not allowed.
	# Function returns how these affect crash rate
	# Return structure:	crash_total	volume_total	percentage	has_structure
	# 					12			100				12			Y
	# 					35			500				7			null
	def structureCrashRelation(self, structure_name):
		if structure_name not in ['ramp', 'bridge', 'railroad crossing', 'one-way']:
			# print("Illegal input!")
			return
		cursor = self.conn.cursor()
		query = """
				SELECT SUM(c.crash_sum) AS crash_total, SUM(c.volume_sum) AS volume_total, SUM(c.crash_sum)/SUM(c.volume_sum)*100 AS percentage, structure FROM
					(SELECT a.municipality, a.county, structure, SUM(crash_count) AS crash_sum, SUM(a.vol) AS volume_sum FROM 
						(SELECT year, municipality, county, {} AS structure, SUM(volume_count) AS vol FROM
						Volume NATURAL JOIN Roads GROUP BY (year, municipality, county, {})) a
					JOIN
						(SELECT year, municipality, county, COUNT(incident_date) AS crash_count FROM Car_crash GROUP BY (year, municipality, county)) b
					ON a.year=b.year and LOWER(a.municipality)=LOWER(b.municipality) and LOWER(a.county)=LOWER(b.county)
					WHERE vol IS NOT NULL
					GROUP BY (a.year, a.municipality, a.county, structure)) c
				GROUP BY structure;
				""".format(structure_name, structure_name)
		cursor.execute(query)
		records = cursor.fetchall()
		return records

	# User inputs a municipality and county name pair, case insensitive. If this pair is not found, return empty.
	# Else return Crashes, Volume and crash rate of every year.
	# Return structure:	year	vol		crash_count	percentage
	# 					2014	9913	108			1.08
	# 					2015	12455	82			0.66
	# 					2016	11676	96			0.82
	def crashRateMunicipality(self, municipality_name, county_name):
		cursor = self.conn.cursor()
		query = """
				SELECT a.year, a.vol, b.crash_count, CAST(b.crash_count AS FLOAT)/CAST(a.vol AS FLOAT)*100 AS percentage FROM 
					(SELECT year, municipality, county, SUM(volume_count) AS vol FROM
					Volume NATURAL JOIN Roads GROUP BY (year, municipality, county)) a
				JOIN
					(SELECT year, municipality, county, COUNT(incident_date) AS crash_count FROM Car_crash GROUP BY (year, municipality, county)) b
				ON a.year=b.year and LOWER(a.municipality)=LOWER(b.municipality) and LOWER(a.county)=LOWER(b.county)
				WHERE a.municipality ILIKE %s and a.county ILIKE%s
				GROUP BY (a.year, a.vol, b.crash_count);
				"""
		cursor.execute(query, (municipality_name, county_name))
		records = cursor.fetchall()
		return records