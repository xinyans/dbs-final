import psycopg2

connection_string = "host='localhost' dbname='dbms_final_project' user='dbms_project_user' password='dbms_password'"

# TODO add your code here (or in other files, at your discretion) to load the data


def main():
    # TODO invoke your code to load the data into the database
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute(open('schema.sql', 'r').read())
    with open('./datasets/Motor_Vehicle_Crashes_-_Case_Information__Three_Year_Window.csv', 'r') as f:
        cursor.copy_expert("COPY Car_crash FROM STDIN WITH CSV HEADER", f)
    conn.commit()

if __name__ == "__main__":
    main()
