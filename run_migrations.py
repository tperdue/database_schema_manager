import os
import sqlite3
from database import create_postgres_connection

# Connect to the SQLite database
conn_sqlite = sqlite3.connect("db/migration_tracker.sqlite")
cursor_sqlite = conn_sqlite.cursor()

# Connect to the PostgreSQL database
conn_postgres = create_postgres_connection()
cursor_postgres = conn_postgres.cursor()

# Select all records where migration_applied is False, ordered by id in ascending order
cursor_sqlite.execute(
    "SELECT * FROM migrations WHERE migration_applied = 'False' ORDER BY id ASC")
results = cursor_sqlite.fetchall()

# Run the migrations
for record in results:
    migration_id = record[0]
    timestamp = record[2]
    migration_folder = f"migrations/changeset{migration_id}_{timestamp}"
    up_file_path = os.path.join(migration_folder, "up.sql")

    # Check if up.sql file exists
    if not os.path.exists(up_file_path):
        print(
            f"Up.sql file for migration {migration_id} not found. Aborting script.")
        break

    # Read and execute the SQL statements in up.sql
    with open(up_file_path, "r") as up_file:
        sql_statements = up_file.read()
        try:
            cursor_postgres.execute(sql_statements)
            migration_status = "Migration successfully applied"
        except Exception as e:
            migration_status = str(e)
            print(
                f"Error occurred while running migration {migration_id}. Aborting script.")
            break

    # Update migration_applied and migration_status columns in SQLite
    cursor_sqlite.execute(
        "UPDATE migrations SET migration_applied = 'True', migration_status = ? WHERE id = ?", (migration_status, migration_id))
    conn_sqlite.commit()

# Commit changes in the PostgreSQL database
conn_postgres.commit()

# Close the database connections
cursor_sqlite.close()
conn_sqlite.close()
cursor_postgres.close()
conn_postgres.close()
