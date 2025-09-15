# Base Image
FROM python:3.13

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend code
COPY . .

# Collect static files (optional)
RUN python manage.py collectstatic --noinput

# Default command: run Gunicorn (web server)
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
