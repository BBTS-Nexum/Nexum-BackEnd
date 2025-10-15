import os
from dotenv import load_dotenv

load_dotenv()

# Tentar importar pymssql primeiro (para Vercel), depois pyodbc (para local)
try:
    import pymssql
    USE_PYMSSQL = True
    print("ℹ️  Usando pymssql (ambiente serverless)")
except ImportError:
    try:
        import pyodbc
        USE_PYMSSQL = False
        print("ℹ️  Usando pyodbc (ambiente local)")
    except ImportError:
        raise ImportError("Nenhum driver SQL disponível. Instale pymssql ou pyodbc.")

# Connection string para pyodbc
conn_str_pyodbc = (
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
    """Conecta ao banco usando pymssql (Vercel) ou pyodbc (local)"""
    if USE_PYMSSQL:
        # pymssql connection
        conn = pymssql.connect(
            server=os.getenv('AZURE_SQL_SERVER'),
            port=int(os.getenv('AZURE_SQL_PORT', '1433')),
            user=os.getenv('AZURE_SQL_USERNAME'),
            password=os.getenv('AZURE_SQL_PASSWORD'),
            database=os.getenv('AZURE_SQL_DATABASE'),
            login_timeout=int(os.getenv('AZURE_SQL_CONNECTION_TIMEOUT', '30')),
            as_dict=False
        )
        return conn
    else:
        # pyodbc connection
        conn = pyodbc.connect(conn_str_pyodbc)
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
    except Exception as e:
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
    except Exception as e:
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
    except Exception as e:
        print(f"Error executing query: {e}")
        return False, None