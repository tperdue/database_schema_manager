import os
import sqlite3
from database import create_postgres_connection

# Connect to the SQLite database
conn_sqlite = sqlite3.connect("db/migration_tracker.sqlite")
cursor_sqlite = conn_sqlite.cursor()

# Connect to the PostgreSQL database
conn_postgres = create_postgres_connection()
cursor_postgres = conn_postgres.cursor()

# Select the last applied migration record
cursor_sqlite.execute(
    "SELECT * FROM migrations WHERE migration_applied = 'True' ORDER BY id DESC LIMIT 1")
record = cursor_sqlite.fetchone()

if record:
    migration_id = record[0]
    timestamp = record[2]
    migration_folder = f"migrations/changeset{migration_id}_{timestamp}"
    down_file_path = os.path.join(migration_folder, "down.sql")

    # Check if down.sql file exists
    if not os.path.exists(down_file_path):
        print(
            f"Down.sql file for migration {migration_id} not found. Aborting script.")
    else:
        # Read and execute the SQL statements in down.sql
        with open(down_file_path, "r") as down_file:
            sql_statements = down_file.read()
            try:
                cursor_postgres.execute(sql_statements)
                migration_status = "Migration was rolled back"
            except Exception as e:
                migration_status = f"Error rolling back migration: {str(e)}"
                print(
                    f"There was an error rolling back migration {migration_id}.\nError message: {str(e)}")

            # Update migration_applied and migration_status columns in SQLite
            cursor_sqlite.execute(
                "UPDATE migrations SET migration_applied = 'False', migration_status = ? WHERE id = ?", (migration_status, migration_id))
            conn_sqlite.commit()

else:
    print("No applied migrations found.")

# Commit changes in the PostgreSQL database
conn_postgres.commit()

# Close the database connections
cursor_sqlite.close()
conn_sqlite.close()
cursor_postgres.close()
conn_postgres.close()
