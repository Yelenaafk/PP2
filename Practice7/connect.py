import psycopg2
from config import db_config

def get_conn():
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        first_name VARCHAR(100),
        phone VARCHAR(20) UNIQUE NOT NULL
    );
    """
    conn = get_conn()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(query)
                conn.commit()
            print("Table check/creation complete.")
        except Exception as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()