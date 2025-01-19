import pandas as pd
import psycopg2

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'spbase'
DB_USER = 'postgres'
DB_PASS = 'pass123'

# Load the CSV data into a DataFrame
csv_file_path = 'C:\New/iot_telemetry_data.csv'
df = pd.read_csv(csv_file_path)

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS
)

# Create a cursor object
cur = conn.cursor()


# Insert DataFrame data into PostgreSQL table
for index, row in df.iterrows():
    insert_query = '''
    INSERT INTO measure (ts, device, co, humidity, light, lpg, motion, smoke, temp)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
    cur.execute(insert_query, tuple(row))
    conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Data loaded successfully!")
