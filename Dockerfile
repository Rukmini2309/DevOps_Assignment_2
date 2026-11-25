# Lightweight Python environment
FROM python:3.12-slim

LABEL description="Flask application for learning Docker and CI"

# Set the application directory
WORKDIR /devops-app

# Install application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application
COPY app.py .

# Document the application port
EXPOSE 5000

# Start the Flask server
CMD ["python", "app.py"]