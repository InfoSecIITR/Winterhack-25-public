FROM python:3.9-slim

WORKDIR /sstiv2_app

COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

RUN useradd -m hacker \
    && chown -R root:root /sstiv2_app \
    && chmod -R 755 /sstiv2_app \
    && chmod -R o-w /sstiv2_app

USER hacker

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
