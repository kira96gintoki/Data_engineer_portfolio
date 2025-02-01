import psycopg2

# Database connection parameters
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'spbase'
DB_USER = 'postgres'
DB_PASS = 'pass123'

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
        with conn.cursor() as cursor:
            # Create schema
            create_schema_query = 'CREATE SCHEMA IF NOT EXISTS spinfo;'
            cursor.execute(create_schema_query)
            conn.commit()
            print("Schema created successfully.")
            
            # Create tables
            create_table1_query = '''
                CREATE TABLE IF NOT EXISTS spinfo.measure (
                    ts INTEGER,
                    device VARCHAR,
                    co DOUBLE PRECISION,
                    humidity DOUBLE PRECISION,
                    light BOOLEAN,
                    lpg DOUBLE PRECISION,
                    motion BOOLEAN,
                    smoke DOUBLE PRECISION,
                    temp VARCHAR
                );
            '''
            cursor.execute(create_table1_query)
            conn.commit()
            print("Table 'measure' created successfully.")

            create_table2_query = '''
                CREATE TABLE IF NOT EXISTS spinfo.sensormetadata (
                    ID INTEGER,
                    location VARCHAR(100),
                    type VARCHAR(100)
                );
            '''
            cursor.execute(create_table2_query)
            conn.commit()
            print("Table 'sensormetadata' created successfully.")

except psycopg2.Error as e:
    print(f"Error setting up database: {e}")

print("Database setup complete!")
