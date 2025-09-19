# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install Flask
RUN pip install --no-cache-dir flask

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
