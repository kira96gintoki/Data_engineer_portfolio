import psycopg2

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'spbase'
DB_USER = 'postgres'
DB_PASS = 'pass123'

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

# Create schema 
create_schema_query = 'CREATE SCHEMA IF NOT EXISTS spinfo;' 
cur.execute(create_schema_query)

# Create tables 
create_table1_query = ''' CREATE TABLE IF NOT EXISTS spinfo.measure ( ts INTEGER, device VARCHAR, co double precision, humidity double precision, light boolean, lpg double precision, motion boolean, smoke double precision, temp VARCHAR ); ''' 
cur.execute(create_measure_query) 
conn.commit() 
create_table2_query = ''' CREATE TABLE IF NOT EXISTS spinfo.sensormetadata ( ID INTEGER, location VARCHAR(100), type VARCHAR(100) ); ''' 
cur.execute(create_sensormetadata_query) 
conn.commit()

cur.close()
conn.close()

print("Database setup complete!")
