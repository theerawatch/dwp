# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Set the working directory to /app/src
WORKDIR /app/src

RUN python manage.py collectstatic --no-input

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variables
ENV DJANGO_SETTINGS_MODULE=dwp_site.settings
ENV PYTHONUNBUFFERED=1

# Run the command to start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]