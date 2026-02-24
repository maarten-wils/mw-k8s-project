# ==============================
# Imports
# ==============================

import os # Used to read environment variables (DB config from Docker/K8S)
import socket # Used to get container hostname (container ID in Docker)
from fastapi import FastAPI, HTTPException # FastAPI app + error handling
import psycopg # PostgreSQL driver, used to connect Python to PostgreSQL

# ==============================
# Create FastAPI application
# ==============================

app = FastAPI() # Main API instance where endpoints are registered

# ==============================
# Database configuration
# ==============================

# Read environment variables injected by Docker.
# If a variable is not set, use the provided default value.

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "mwdb")
DB_USER = os.getenv("DB_USER", "mw")
DB_PASSWORD = os.getenv("DB_PASSWORD", "class")

# ==============================
# Database connection function
# ==============================

# Opens a new database connection.
# A new connection per request is simple and robust for small projects.

def connect_to_database():
    return psycopg.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )

# ==============================
# Endpoint: Get user name from database
# ==============================
# This endpoint:
# 1. Opens a database connection
# 2. Executes a SELECT query
# 3. Returns the first user's name
# 4. Handles possible errors

@app.get("/user")
def get_user():
    try:
        with connect_to_database() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM users;")
                row = cursor.fetchone()
                if not row:
                    raise HTTPException(status_code=404, detail="No user found in DB")
                return {"name": row[0]}
    except psycopg.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

# ==============================
# Endpoint: Get container ID
# ==============================

# Returns the container hostname.
# In Docker, hostname = container ID.

@app.get("/container")
def get_container():
    return {"id": socket.gethostname()}





