import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn_str = (
    f"DRIVER={{{os.getenv('AZURE_SQL_DRIVER')}}};"
    f"SERVER={os.getenv('AZURE_SQL_SERVER')},{os.getenv('AZURE_SQL_PORT')};"
    f"DATABASE={os.getenv('AZURE_SQL_DATABASE')};"
    f"UID={os.getenv('AZURE_SQL_USERNAME')};"
    f"PWD={os.getenv('AZURE_SQL_PASSWORD')};"
    f"Encrypt={os.getenv('AZURE_SQL_ENCRYPT')};"
    f"TrustServerCertificate={os.getenv('AZURE_SQL_TRUST_SERVER_CERTIFICATE')};"
    f"Connection Timeout={os.getenv('AZURE_SQL_CONNECTION_TIMEOUT')};"
)


def connect():
    conn = pyodbc.connect(conn_str)
    return conn

def execute_fetch_all(query, params=None):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return True, results
    except pyodbc.Error as e:
        print(f"Error executing query: {e}")
        return False, []

def execute_commit(query, params=None):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except pyodbc.Error as e:
        print(f"Error executing command: {e}")
        return False

def execute_one_fetch(query, params=None):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return True, result
    except pyodbc.Error as e:
        print(f"Error executing query: {e}")
        return False, None