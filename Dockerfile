
# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .

# Copy HTML templates
COPY templates/ ./templates/

# Expose Flask port
EXPOSE 8080

# Start application
CMD ["python", "app.py"]
