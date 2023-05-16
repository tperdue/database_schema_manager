import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def create_postgres_connection():
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
