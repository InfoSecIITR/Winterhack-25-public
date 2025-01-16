# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /sstiv1_app

# Copy the requirements.txt file into the container
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

RUN useradd -m hacker \
    && chown -R root:root /sstiv1_app \
    && chmod -R 755 /sstiv1_app \
    && chmod -R o-w /sstiv1_app

USER hacker

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
