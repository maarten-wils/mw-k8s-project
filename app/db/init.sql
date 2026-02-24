-- This script is executed automatically by the PostgreSQL container image ONLY during the first initialization of the database directory.
-- It runs when the data volume is empty. If the container is restarted, this script will NOT run again. To force re-exection, you must remove
-- the volume (e.g. "docker compose down -v")

-- Create table only if it doesn't exist yet

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Insert initial value

INSERT INTO users (name) VALUES ('Maarten');