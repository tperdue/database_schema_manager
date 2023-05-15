import os
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("db/migration_tracker.sqlite")
cursor = conn.cursor()

# Select all records where migration_applied is False, ordered by id in ascending order
cursor.execute(
    "SELECT * FROM migrations WHERE migration_applied = 'False' ORDER BY id ASC")
results = cursor.fetchall()

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
            cursor.executescript(sql_statements)
            migration_status = "Migration successfully applied"
        except Exception as e:
            migration_status = str(e)
            print(
                f"Error occurred while running migration {migration_id}. Aborting script.")
            break

    # Update migration_applied and migration_status columns
    cursor.execute("UPDATE migrations SET migration_applied = 'True', migration_status = ? WHERE id = ?",
                   (migration_status, migration_id))
    conn.commit()

# Close the database connection
cursor.close()
conn.close()
