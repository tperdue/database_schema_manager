import sqlite3
from datetime import datetime

class MigrationTracker:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_database(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS migration_tracker")

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                id INTEGER PRIMARY KEY,
                description TEXT,
                timestamp TEXT,
                migration_applied TEXT
            )
        """)

    def check_database_and_table(self):
        self.create_database()
        self.create_table()

    def insert_migration(self, description):
        timestamp = str(datetime.now())
        migration_applied = "False"
        self.cursor.execute("INSERT INTO migrations (description, timestamp, migration_applied) VALUES (?, ?, ?)",
                            (description, timestamp, migration_applied))
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

def main():
    db_name = "dbs/migration_tracker.sqlite"
    tracker = MigrationTracker(db_name)
    tracker.check_database_and_table()
    print("Migration tracker setup completed.")

if __name__ == "__main__":
    main()
