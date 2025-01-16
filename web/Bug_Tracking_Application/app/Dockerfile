FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose Flask app
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-k", "gevent"]