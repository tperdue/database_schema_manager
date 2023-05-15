import os
import sqlite3
from datetime import datetime

# Prompt the user for a description of the migration
description = input("Enter the description of the migration: ")

# Connect to the SQLite database
conn = sqlite3.connect("db/migration_tracker.sqlite")
cursor = conn.cursor()

# Get the highest existing migration id
cursor.execute("SELECT MAX(id) FROM migrations")
result = cursor.fetchone()
highest_id = result[0] if result[0] else 0

# Increment the id and get the current timestamp
migration_id = highest_id + 1
timestamp = int(datetime.now().timestamp())

# Insert a new row into the migrations table
migration_applied = str(False)
cursor.execute("INSERT INTO migrations (id, description, timestamp, migration_applied) VALUES (?, ?, ?, ?)",
               (migration_id, description, timestamp, migration_applied))
conn.commit()

# Create the migration folder
folder_name = f"changeset{migration_id}_{timestamp}"
os.makedirs(f"migrations/{folder_name}")

# Create the up.sql file
with open(f"migrations/{folder_name}/up.sql", "w") as up_file:
    up_file.write(f"-- Migration for: {description}\n")

# Create the down.sql file
with open(f"migrations/{folder_name}/down.sql", "w") as down_file:
    down_file.write(f"-- Rollback for: {description}\n")

# Create the README.md file with instructions
readme_content = f"""# Migration Instructions

To apply this migration, follow these steps:

1. Create a feature branch with the migration folder name as the branch name:
   ```bash
   git checkout -b {folder_name}
   ```

2. Add only the migration folder that was created to the commit:
    ```bash
    git add migrations/{folder_name}
    ```

3. Commit the changes with the description as the commit message:
    ```bash
    git commit -m "{description}"
    ```

4. Push the commit to the remote repository named origin:
    ```bash
    git push origin {folder_name}
    ```

5. Create a pull request and wait for it to be approved and merged into the main branch.

6. After the pull request is merged, you can delete the local and remote feature branches:
    ```bash
    git branch -d {folder_name}
    git push origin --delete {folder_name}
"""

with open(f"migrations/{folder_name}/git_workflow.md", "w") as readme_file:
    readme_file.write(readme_content)

cursor.close()
conn.close()
