import os
from dotenv import load_dotenv
from mssql_python import mssql

load_dotenv()

def connect():
    """Conecta ao banco usando mssql-python"""
    conn = mssql.connect(
        server=os.getenv('AZURE_SQL_SERVER'),
        port=int(os.getenv('AZURE_SQL_PORT', '1433')),
        user=os.getenv('AZURE_SQL_USERNAME'),
        password=os.getenv('AZURE_SQL_PASSWORD'),
        database=os.getenv('AZURE_SQL_DATABASE'),
        login_timeout=int(os.getenv('AZURE_SQL_CONNECTION_TIMEOUT', '30')),
        as_dict=False
    )
    return conn

def execute_fetch_all(query, params=None):
    """Executa uma query e retorna todos os resultados"""
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return True, results
    except Exception as e:
        print(f"Erro ao executar query: {e}")
        return False, []

def execute_commit(query, params=None):
    """Executa uma query de modificação (INSERT, UPDATE, DELETE)"""
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao executar comando: {e}")
        return False

def execute_one_fetch(query, params=None):
    """Executa uma query e retorna apenas o primeiro resultado"""
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return True, result
    except Exception as e:
        print(f"Erro ao executar query: {e}")
        return False, None