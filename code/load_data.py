import psycopg2

connection_string = "host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password'"

# TODO add your code here (or in other files, at your discretion) to load the data


def main():
    # TODO invoke your code to load the data into the database
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    print('Creating schemas...')
    cursor.execute(open('schema.sql', 'r').read())
    print('Copying crashes table...')
    with open('./datasets/Motor_Vehicle_Crashes_-_Case_Information__Three_Year_Window.csv', 'r') as f:
        cursor.copy_expert("COPY Car_crash FROM STDIN WITH CSV HEADER", f)
    print('Copying traffic volume table...')
    with open('./datasets/Annual_Average_Daily_Traffic__AADT___Beginning_1977.csv', 'r') as f:
        cursor.copy_expert("COPY Location_volume_temp FROM STDIN WITH CSV HEADER", f)
    print('Populating entries to volume table...')
    cursor.execute("""
        INSERT INTO Volume
        SELECT year, station_ID, volume_count FROM Location_volume_temp
        ON CONFLICT DO NOTHING
    """)
    print('Populating entries to roads table...')
    cursor.execute("""
        INSERT INTO Roads
        SELECT station_ID, MIN(county), MIN(signing), MIN(state_route), 
        MIN(county_road), MIN(road_name), MIN(beginning_description), 
        MIN(ending_description), MIN(municipality), MIN(length), 
        MIN(functional_class), MIN(ramp), MIN(bridge), MIN(railroad_crossing), 
        MIN(one_way) FROM Location_volume_temp GROUP BY station_ID
        ON CONFLICT DO NOTHING
    """)
    conn.commit()
    print('Dropping temp table...')
    cursor.execute('DROP TABLE Location_volume_temp')
    conn.commit()

if __name__ == "__main__":
    main()
