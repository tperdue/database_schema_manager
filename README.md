# Database Schema Manager

Database Schema Manager is a lightweight tool designed to track and manage schema changes for your database using SQL scripts. It allows you to version control your schema changes using Git and provides flexibility to work with different databases.


## Project Overview

The Database Schema Manager project provides the following components:

- `db/` directory: Contains the `migration_tracker.sqlite` file, which serves as the local SQLite database for tracking migrations.

- `migrations/` directory: Stores the SQL files documenting the schema changes for your database. Each file represents a specific schema change, and they are executed in order.

- `.env.example` file: A template file that can be used to set up environment variables for connecting to the target database. Please remember to add your .env file to the .gitignore file to prevent it from being committed to your repo.

- `.gitignore` file: Specifies files and directories to be ignored by Git, preventing them from being committed to the repository.

- `create_migration.py` script: Allows you to create a new migration by prompting for a description and generating the necessary files and folder structure.

- `database.py` module: Provides functions to establish connections with different databases, such as PostgreSQL and MySQL, allowing you to apply schema changes to the target database.

- `README.md` file: The document you are currently reading, providing an overview of the project and instructions for usage.

- `requirements.txt` file: Lists the required Python packages and their versions for this project.

- `rollback_migration.py` script: Allows you to roll back the last applied migration by executing the associated `down.sql` file.

- `run_migrations.py` script: Executes the unapplied migrations, applying the schema changes to the target database.

- `setup_migration_tracker.py` script: Sets up the migration tracker utility by creating the `migrations` table in the `migration_tracker.sqlite` database.


## Usage

To utilize the Database Schema Manager, follow the instructions below:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/database-schema-manager.git
   ```

2. Set up the migration tracker utility by running the following command:

   ```bash
   python setup_migration_tracker.py
   ```
   This script will create the necessary table in the migration_tracker.sqlite database.

3. Create a new migration using the `create_migration.py` script. It will prompt you for a description, generate the required files and folder structure, and create a new entry in the migrations table.

   ```bash
   python create_migration.py
   ```

4. Execute the unapplied migrations by running the `run_migrations.py` script. It will read the migrations table, locate the associated `up.sql` file for each migration, and apply the schema changes to the target database.

   ```bash
   python run_migrations.py
   ```

5. If needed, roll back the last applied migration using the `rollback_migration.py` script. It will identify the associated `down.sql` file and execute the necessary SQL statements to revert the schema changes.

   ```bash
   python rollback_migration.py
   ```
6. After completing the necessary steps, you can continue working with the Database Schema Manager to create and execute additional migrations as needed.



## Supported Databases

The Database Schema Manager supports various databases by utilizing the appropriate connection libraries. By default, it uses a local SQLite database for tracking migrations. However, you can extend the functionality to work with other popular databases. Below are examples of how to connect to different databases:

### PostgreSQL

To use PostgreSQL as the target database, ensure you have the `psycopg2` library installed. Update the `database.py` module with the following code:

```python
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def create_postgres_connection():
    # Retrieve database connection details from environment variables or other configuration methods
    host = os.getenv("PG_HOST")
    port = os.getenv("PG_PORT")
    database = os.getenv("PG_DATABASE")
    user = os.getenv("PG_USER")
    password = os.getenv("PG_PASSWORD")

    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    return conn
```


Modify the code as per your specific PostgreSQL configuration. With this updated code, you can establish a connection to a PostgreSQL database by calling `create_postgres_connection()`.

You can apply similar modifications to connect with other databases like MySQL or SQL Server by utilizing the appropriate libraries and adjusting the connection code accordingly.

Please note that you may need to install the respective database client libraries and configure the necessary environment variables to establish connections with different databases.


## Project Background

The Database Schema Manager project was born out of the desire to use SQL for writing schema changes without relying on an ORM. It also aims to version control schema changes using Git while keeping the tooling minimal and lightweight.

The tool provides a simple yet effective way to track and manage schema changes for your database, allowing you to maintain a clear history of modifications and apply them consistently across different environments.

Please note that the Database Schema Manager is designed to be a lightweight solution and may not have the same level of robustness as full-fledged database migration tools. It serves as a flexible and easy-to-use option for small to medium-sized projects.

If you encounter any issues or have suggestions for improvements, I appreciate your feedback! While I may not actively manage pull requests or actively develop the project further, I encourage you to share your ideas by opening an issue or forking the repository to modify the project according to your needs. I welcome any contributions that enhance the functionality or address any concerns. Thank you for your support and understanding!


## License

The Database Schema Manager project is licensed under the [MIT License](./LICENSE). You are free to use, modify, and distribute the code to suit your needs.

## Acknowledgements

We would like to express our gratitude to all the contributors who have helped with the development and maintenance of the Database Schema Manager project.

## Contact

If you have any questions or need further assistance, please contact our support team at support@yourcompany.com.


