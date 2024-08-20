# Use the official Python image from the Docker Hub
FROM python:3.12.1-alpine3.19@sha256:28230397c48cf4e2619822beb834ae7e46ebcd255b8f7cef58eff932fd75d2ce

# Set environment variables to ensure Python runs in unbuffered mode
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies and create virtual environment
# postgresql-dev is also added incase postgres or supabase is used
RUN apk add --no-cache \
    python3-dev \
    libffi-dev \
    gcc \
    musl-dev \
    postgresql-dev \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip

# Set environment variables for virtual environment
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
