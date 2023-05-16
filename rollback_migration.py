import os
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("db/migration_tracker.sqlite")
cursor = conn.cursor()

# Select the last applied migration record
cursor.execute(
    "SELECT * FROM migrations WHERE migration_applied = 'True' ORDER BY id DESC LIMIT 1")
record = cursor.fetchone()

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
                cursor.executescript(sql_statements)
                migration_status = "Migration was rolled back"
                cursor.execute(
                    "UPDATE migrations SET migration_applied = 'False', migration_status = ? WHERE id = ?", (migration_status, migration_id))
                conn.commit()
                print(
                    f"Migration {migration_id} was successfully rolled back.")
            except Exception as e:
                migration_status = f"Error rolling back migration: {str(e)}"
                cursor.execute(
                    "UPDATE migrations SET migration_status = ? WHERE id = ?", (migration_status, migration_id))
                conn.commit()
                print(
                    f"There was an error rolling back migration {migration_id}.")
else:
    print("No applied migrations found.")

# Close the database connection
cursor.close()
conn.close()
