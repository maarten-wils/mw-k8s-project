# Official Python image (slim = smaller image size)
FROM python:3.12-slim

WORKDIR /app

# Install libpq so psycopg can compile cleanly
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000

# Run uvicorn when container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]