# Client Web App Schema Changes

This repository contains the SQL files documenting the schema changes for the Client Web App. These files provide a historical record of the modifications made to the database schema over time.

## Schema Change Files

The following SQL files can be found in the repository:

- [change001.sql](./change001.sql): This file contains the SQL script for the first schema change.
- [change002.sql](./change002.sql): This file contains the SQL script for the second schema change.
- [change003.sql](./change003.sql): This file contains the SQL script for the third schema change.
- ...

Feel free to browse through the SQL files to understand the specific modifications made to the database schema.

## Usage

To apply the schema changes to your local database, follow these steps:

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/your-username/client-web-app-schema-changes.git
    ```


2. Connect to your database using a SQL client or command-line interface.

3. Execute the SQL files in the order of their filenames (e.g., `change001.sql`, `change002.sql`, etc.), applying each schema change to the database. If you are using a command-line interface, you can execute the SQL files using a command similar to the following:

    ```bash
        psql -U your-username -d your-database-name -f change001.sql
    ```
    Replace `your-username` with your database username and `your-database-name` with the name of your database.

    Make sure to apply the schema changes in the correct order to maintain data integrity and prevent any potential issues.


## Setup Migration Tracker Utility

To set up the migration tracker utility for managing schema changes, run the following command:

```bash
python setup_migration_utility
```

This script checks the `dbs` directory to see if there is a SQLite database named `migration_tracker`. If the database doesn't exist, it creates the database. It also checks if the `migration_tracker` database has a table named `migrations`. If the table doesn't exist, it creates the table with the following columns:

- `id` (an integer that goes up to 1 million)
- `description` (a text field)
- `timestamp` (a timestamp field or string representation of a timestamp)
- `migration_applied` (a boolean field or string representation of a boolean that can be recognized by Python as a boolean)

This utility helps track and manage migrations in the Client Web App.


## Contributing

If you discover any issues or have suggestions for improvements, please feel free to [open an issue](https://github.com/your-username/client-web-app-schema-changes/issues) or submit a pull request. Your contributions are highly appreciated!

## License

This repository is licensed under the [MIT License](./LICENSE). Feel free to use the code and adapt it to your needs.

## Acknowledgements

We would like to thank all contributors who have helped with the development and maintenance of the Client Web App schema changes.

## Contact

If you have any questions or need further assistance, please contact our support team at support@clientwebapp.com.
