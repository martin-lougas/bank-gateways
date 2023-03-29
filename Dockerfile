# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY app app

# Copy the certificate and key files into the container at /app/cert
COPY app/cert/certificate.pem app/cert/certificate.key /app/cert/

# Expose the port that the application will listen on
EXPOSE 80

# Set the environment variable to specify the path to the certificate and key files
ENV CERT_DIR=/app/cert

# Start the application server using uvicorn
CMD ["uvicorn", "app.main:app", "--ssl-certfile", "/app/cert/certificate.pem", "--ssl-keyfile", "/app/cert/certificate.key", "--host", "0.0.0.0", "--port", "80"]
