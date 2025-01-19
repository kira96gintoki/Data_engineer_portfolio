FROM python:3.12
# Set the working directory
WORKDIR C:\New

# Install dependencies for PostgreSQL and Python
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*



# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY iot_telemetry_data.csv /app/iot_telemetry_data.csv

# Run the Python script to load the CSV into the database
CMD ["python", "load_data.py", "uvicorn", "app.main:app", "--host", "localhost", "--port", "5432"]

