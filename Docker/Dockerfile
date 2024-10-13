# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary Python packages (flask)
RUN pip install --no-cache-dir flask

# Expose port 5000 to allow external connections to the Flask app
EXPOSE 5000

# Set environment variable to avoid issues with Python stdout buffering
ENV PYTHONUNBUFFERED=1

# Run the Flask app
CMD ["python", "myapp.py"]
