# Base image optimized for Raspberry Pi
FROM python:3.11-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies for Python, GPIO, and PostgreSQL
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libgpiod-dev \
    libpq-dev \
    postgresql-client \
    ntpdate \
    curl \
    libcairo2-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
#RUN ntpdate pool.ntp.org
# Install Django 5 and Python dependencies
COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./static /app/static
COPY ./transactify_terminal /app/

RUN chmod +x /app/entrypoint.sh 

# Expose the application port
EXPOSE 8000

# Run migrations and start the Django development server
ENTRYPOINT ["/app/entrypoint.sh"]