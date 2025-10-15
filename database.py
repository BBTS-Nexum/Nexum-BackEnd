import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv('AZURE_SQL_SERVER')
DATABASE = os.getenv('AZURE_SQL_DATABASE')
USERNAME = os.getenv('AZURE_SQL_USERNAME')
PASSWORD = os.getenv('AZURE_SQL_PASSWORD')

CONNECTION_STRING = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'UID={USERNAME};'
    f'PWD={PASSWORD}'
)

def get_db_connection():
    try:
        conn = pyodbc.connect(CONNECTION_STRING)
        return conn
    except pyodbc.Error as e:
        print(f"Erro na conexão com Azure SQL: {e}")
        return None 

def fetch_all(query, params=None):

    conn = get_db_connection()
    if not conn: return []
        
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    columns = [column[0] for column in cursor.description]
    data = []
    for row in cursor.fetchall():
        data.append(dict(zip(columns, row)))
    conn.close()
    return data

def fetch_one(query, params=None):

    conn = get_db_connection()
    if not conn: return None
        
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    columns = [column[0] for column in cursor.description]
    data = cursor.fetchone()
    conn.close()
    
    return dict(zip(columns, data)) if data else None

def execute_query(query, params=None):

    conn = get_db_connection()
    if not conn: 
        return False, "Erro de conexão com o banco de dados."
        
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        rows_affected = cursor.rowcount
        conn.close()
        return True, rows_affected
    except pyodbc.Error as e:
        conn.rollback()
        conn.close()
        
        print(f"Erro ao executar query: {e}") 
        return False, "Falha na operação do banco de dados."