import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="inference_db",
        user="inference_user",
        password="password",
        host="localhost",
        port=5432
    )
