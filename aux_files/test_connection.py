"""
Script de Teste de Conexão - Azure SQL Database
Autor: BBTS Nexum Team
Data: 2025-10-15

Este script testa a conexão com o Azure SQL Database
usando as configurações do arquivo .env
"""

import pyodbc
from dotenv import load_dotenv
import os
import sys

# Carregar variáveis de ambiente
load_dotenv()

def test_connection():
    """Testa a conexão com o Azure SQL Database"""
    
    print("=" * 80)
    print("🔧 TESTE DE CONEXÃO - AZURE SQL DATABASE")
    print("=" * 80)
    
    # Verificar se as variáveis estão configuradas
    print("\n📋 Verificando configurações do .env...")
    
    required_vars = [
        'AZURE_SQL_DRIVER',
        'AZURE_SQL_SERVER',
        'AZURE_SQL_PORT',
        'AZURE_SQL_DATABASE',
        'AZURE_SQL_USERNAME',
        'AZURE_SQL_PASSWORD'
    ]
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if not value or value.startswith('seu-'):
            missing_vars.append(var)
            print(f"   ❌ {var}: NÃO CONFIGURADO")
        else:
            # Mascarar senha
            if 'PASSWORD' in var:
                masked_value = '*' * len(value)
                print(f"   ✅ {var}: {masked_value}")
            else:
                print(f"   ✅ {var}: {value}")
    
    if missing_vars:
        print("\n❌ ERRO: Variáveis não configuradas!")
        print("\n📝 Passos para corrigir:")
        print("   1. Copie o arquivo .env.example para .env")
        print("   2. Edite o arquivo .env com suas credenciais do Azure")
        print("   3. Execute este script novamente")
        print("\n💡 Consulte o arquivo CONFIGURAR_AZURE.md para mais detalhes")
        return False
    
    # Montar connection string
    driver = os.getenv('AZURE_SQL_DRIVER')
    server = os.getenv('AZURE_SQL_SERVER')
    port = os.getenv('AZURE_SQL_PORT')
    database = os.getenv('AZURE_SQL_DATABASE')
    username = os.getenv('AZURE_SQL_USERNAME')
    password = os.getenv('AZURE_SQL_PASSWORD')
    encrypt = os.getenv('AZURE_SQL_ENCRYPT', 'yes')
    trust_cert = os.getenv('AZURE_SQL_TRUST_SERVER_CERTIFICATE', 'no')
    timeout = os.getenv('AZURE_SQL_CONNECTION_TIMEOUT', '30')
    
    conn_str = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server},{port};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        f"Encrypt={encrypt};"
        f"TrustServerCertificate={trust_cert};"
        f"Connection Timeout={timeout};"
    )
    
    # Tentar conectar
    print("\n🔄 Tentando estabelecer conexão...")
    print(f"   Servidor: {server}:{port}")
    print(f"   Database: {database}")
    print(f"   Usuário: {username}")
    print(f"   Timeout: {timeout}s")
    
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # Testar queries básicas
        print("\n✅ CONEXÃO ESTABELECIDA COM SUCESSO!")
        
        # Versão do SQL Server
        print("\n📊 Informações do Servidor:")
        cursor.execute("SELECT @@VERSION")
        version = cursor.fetchone()[0]
        print(f"\n{version}")
        
        # Nome do database atual
        cursor.execute("SELECT DB_NAME()")
        db_name = cursor.fetchone()[0]
        print(f"\n📁 Database Atual: {db_name}")
        
        # Verificar schema supply_chain
        cursor.execute("""
            SELECT SCHEMA_NAME 
            FROM INFORMATION_SCHEMA.SCHEMATA 
            WHERE SCHEMA_NAME = 'supply_chain'
        """)
        schema_exists = cursor.fetchone()
        
        if schema_exists:
            print(f"✅ Schema 'supply_chain' existe")
            
            # Verificar tabelas
            cursor.execute("""
                SELECT TABLE_NAME 
                FROM INFORMATION_SCHEMA.TABLES 
                WHERE TABLE_SCHEMA = 'supply_chain'
                ORDER BY TABLE_NAME
            """)
            tables = cursor.fetchall()
            
            if tables:
                print(f"\n📊 Tabelas encontradas no schema 'supply_chain':")
                for table in tables:
                    cursor.execute(f"""
                        SELECT COUNT(*) 
                        FROM supply_chain.{table[0]}
                    """)
                    count = cursor.fetchone()[0]
                    print(f"   - {table[0]}: {count:,} registros")
            else:
                print("⚠️ Nenhuma tabela encontrada no schema 'supply_chain'")
                print("\n💡 Execute os scripts SQL para criar as tabelas:")
                print("   1. database/create_table.sql")
                print("   2. database/create_users_table.sql")
        else:
            print("⚠️ Schema 'supply_chain' não existe ainda")
            print("\n💡 Execute os scripts SQL para criar o schema e tabelas:")
            print("   1. database/create_table.sql")
            print("   2. database/create_users_table.sql")
        
        # Testar permissões
        print("\n🔐 Testando permissões...")
        try:
            cursor.execute("CREATE TABLE ##test_temp (id INT)")
            cursor.execute("DROP TABLE ##test_temp")
            print("   ✅ Permissões de CREATE TABLE: OK")
        except Exception as e:
            print(f"   ⚠️ Permissões limitadas: {str(e)[:100]}")
        
        conn.close()
        
        print("\n" + "=" * 80)
        print("🎉 TESTE CONCLUÍDO COM SUCESSO!")
        print("=" * 80)
        print("\n✅ Sua conexão com o Azure SQL Database está funcionando perfeitamente!")
        print("\n📝 Próximos passos:")
        print("   1. Se as tabelas não existem, execute os scripts SQL no Azure:")
        print("      - database/create_table.sql")
        print("      - database/create_users_table.sql")
        print("   2. Popule os dados com: python database/insert_data.py")
        print("   3. Teste o gerenciador de usuários: python database/user_manager.py")
        print("\n")
        
        return True
        
    except pyodbc.Error as e:
        print("\n❌ ERRO AO CONECTAR!")
        print("\n🔍 Detalhes do erro:")
        print(f"   {str(e)}")
        
        # Sugestões baseadas no erro
        error_msg = str(e).lower()
        
        print("\n💡 Possíveis soluções:")
        
        if 'login failed' in error_msg:
            print("   1. ❌ Username ou Password incorretos")
            print("   2. Verifique as credenciais no arquivo .env")
            print("   3. Teste fazer login no Azure Portal com essas credenciais")
            print("   4. O username pode precisar ou não do sufixo @servidor")
        
        elif 'cannot open server' in error_msg or 'timeout' in error_msg:
            print("   1. ❌ Servidor inacessível ou firewall bloqueando")
            print("   2. Verifique se o firewall do Azure permite seu IP")
            print("   3. No Portal Azure: SQL Server > Networking > Add client IP")
            print("   4. Verifique sua conexão com a internet")
        
        elif 'data source name not found' in error_msg:
            print("   1. ❌ Driver ODBC não encontrado")
            print("   2. Instale o ODBC Driver 18 for SQL Server")
            print("   3. Download: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server")
            print("   4. Verifique drivers instalados: Get-OdbcDriver (PowerShell)")
        
        elif 'certificate' in error_msg or 'ssl' in error_msg:
            print("   1. ❌ Problema com certificado SSL")
            print("   2. Tente alterar no .env:")
            print("      AZURE_SQL_TRUST_SERVER_CERTIFICATE=yes")
            print("   3. (Menos seguro, use apenas para testes)")
        
        else:
            print("   1. Consulte o guia completo: CONFIGURAR_AZURE.md")
            print("   2. Verifique se todas as configurações estão corretas")
            print("   3. Teste a conexão usando Azure Data Studio")
        
        print("\n")
        return False
    
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {str(e)}")
        return False


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
