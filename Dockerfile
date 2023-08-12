# Use the official Python image as the base image
FROM python:3.10-slim

# Install system dependencies for psycopg2
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the FastAPI server will be running on
EXPOSE 8080

# Start the FastAPI server using uvicorn
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8080"]
