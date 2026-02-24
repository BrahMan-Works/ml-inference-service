import os
import time
import psycopg2
import logging

from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

connection_pool = None

def init_connection_pool():
    global connection_pool

    for attempt in range(10):
        try:
            connection_pool = pool.SimpleConnectionPool(
                minconn=1,
                maxconn=10,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT,
            )
            logging.info("Database connection pool created")
            return
        except psycopg2.OperationalError as e:
            logging.info(f"Database not ready. Retrying... ({attempt+1}/10)")
            time.sleep(2)

    raise Exception("Failed to connect to database after retries.")

def get_connection():
    if connection_pool is None:
        raise Exception("Connection pool not initialized")
    return connection_pool.getconn()

def release_connection(conn):
    connection_pool.putconn(conn)
