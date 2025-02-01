import pandas as pd
import psycopg2

# Database connection parameters
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'spbase'
DB_USER = 'postgres'
DB_PASS = 'pass123'

# Load the CSV data into a DataFrame
csv_file_path = 'C:/New/iot_telemetry_data.csv'
df = pd.read_csv(csv_file_path)

try:
    # Establish a connection to the PostgreSQL database using a context manager
    with psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    ) as conn:
        # Create a cursor object using a context manager
        with conn.cursor() as cur:
            # Insert DataFrame data into PostgreSQL table
            for index, row in df.iterrows():
                insert_query = '''
                INSERT INTO spinfo.measure (ts, device, co, humidity, light, lpg, motion, smoke, temp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                '''
                cur.execute(insert_query, tuple(row))
            
            # Commit the transaction
            conn.commit()
            print("Data loaded successfully.")

except psycopg2.Error as e:
    print(f"Error loading data into database: {e}")

print("Database load complete!")
