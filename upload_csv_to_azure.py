"""
Script para upload de dados do CSV para Azure SQL Database
Database: stefanini_app
Schema: supply_chain
Table: produtos_estoque

Uso:
    python upload_csv_to_azure.py
"""

import pandas as pd
import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do banco de dados
DB_CONFIG = {
    'driver': os.getenv('AZURE_SQL_DRIVER', 'ODBC Driver 18 for SQL Server'),
    'server': os.getenv('AZURE_SQL_SERVER'),
    'port': os.getenv('AZURE_SQL_PORT', '1433'),
    'database': os.getenv('AZURE_SQL_DATABASE'),
    'username': os.getenv('AZURE_SQL_USERNAME'),
    'password': os.getenv('AZURE_SQL_PASSWORD'),
    'encrypt': os.getenv('AZURE_SQL_ENCRYPT', 'yes'),
    'trust_server_certificate': os.getenv('AZURE_SQL_TRUST_SERVER_CERTIFICATE', 'no'),
    'connection_timeout': os.getenv('AZURE_SQL_CONNECTION_TIMEOUT', '30')
}

# Caminho do arquivo CSV
CSV_FILE = 'dados_hackathon.csv'

def get_connection_string():
    """Gera a connection string para o Azure SQL"""
    return (
        f"Driver={{{DB_CONFIG['driver']}}};"
        f"Server=tcp:{DB_CONFIG['server']},{DB_CONFIG['port']};"
        f"Database={DB_CONFIG['database']};"
        f"Uid={DB_CONFIG['username']};"
        f"Pwd={DB_CONFIG['password']};"
        f"Encrypt={DB_CONFIG['encrypt']};"
        f"TrustServerCertificate={DB_CONFIG['trust_server_certificate']};"
        f"Connection Timeout={DB_CONFIG['connection_timeout']};"
    )

def limpar_tabela(cursor):
    """Limpa todos os registros da tabela (opcional)"""
    print("⚠️  Limpando tabela supply_chain.produtos_estoque...")
    cursor.execute("DELETE FROM supply_chain.produtos_estoque")
    print("✅ Tabela limpa com sucesso!")

def validar_dados(df):
    """Valida os dados do CSV antes de inserir"""
    print("\n📋 Validando dados do CSV...")
    
    erros = []
    
    # Verificar colunas obrigatórias
    colunas_obrigatorias = ['codigo', 'abc', 'tipo', 'cmm']
    for col in colunas_obrigatorias:
        if col not in df.columns:
            erros.append(f"Coluna obrigatória ausente: {col}")
    
    if erros:
        for erro in erros:
            print(f"❌ {erro}")
        return False
    
    # Validar ABC
    valores_abc_invalidos = df[~df['abc'].isin(['A', 'B', 'C'])]['abc'].unique()
    if len(valores_abc_invalidos) > 0:
        print(f"⚠️  Valores ABC inválidos encontrados: {valores_abc_invalidos}")
        print("   Valores aceitos: A, B, C")
        return False
    
    # Validar Tipo
    valores_tipo_invalidos = df[~df['tipo'].isin([10, 19, 20])]['tipo'].unique()
    if len(valores_tipo_invalidos) > 0:
        print(f"⚠️  Valores de Tipo inválidos encontrados: {valores_tipo_invalidos}")
        print("   Valores aceitos: 10, 19, 20")
        return False
    
    # Validar duplicatas
    duplicatas = df[df.duplicated(subset=['codigo'], keep=False)]
    if not duplicatas.empty:
        print(f"⚠️  Códigos duplicados encontrados: {duplicatas['codigo'].unique()}")
        return False
    
    print("✅ Validação concluída com sucesso!")
    return True

def preparar_dados(df):
    """Prepara os dados do CSV para inserção"""
    print("\n🔄 Preparando dados para inserção...")
    
    # O CSV já vem com nomes de colunas corretos (minúsculas e snake_case)
    # Apenas garantir que estão no formato esperado
    df_prep = df.copy()
    
    # Preencher valores nulos com 0 para colunas numéricas
    colunas_numericas = [
        'saldo_manut', 'provid_compras', 'recebimento_esperado',
        'transito_manut', 'stage_manut', 'recepcao_manut', 'pendente_ri',
        'pecas_teste_kit', 'pecas_teste', 'fornecedor_reparo', 'laboratorio',
        'wr', 'wrcr', 'stage_wr', 'cmm', 'coef_perda'
    ]
    
    for col in colunas_numericas:
        if col in df_prep.columns:
            df_prep[col] = pd.to_numeric(df_prep[col], errors='coerce').fillna(0)
    
    # Garantir tipos corretos
    df_prep['abc'] = df_prep['abc'].astype(str).str.upper()
    df_prep['tipo'] = df_prep['tipo'].astype(int)
    df_prep['codigo'] = df_prep['codigo'].astype(str)
    
    print(f"✅ {len(df_prep)} registros preparados!")
    return df_prep

def inserir_dados(cursor, df):
    """Insere os dados no banco de dados"""
    print("\n📤 Inserindo dados no Azure SQL...")
    
    # Query de inserção
    insert_query = """
    INSERT INTO supply_chain.produtos_estoque (
        codigo, abc, tipo, saldo_manut, provid_compras, recebimento_esperado,
        transito_manut, stage_manut, recepcao_manut, pendente_ri,
        pecas_teste_kit, pecas_teste, fornecedor_reparo, laboratorio,
        wr, wrcr, stage_wr, cmm, coef_perda,
        data_criacao, data_atualizacao, usuario_criacao, usuario_atualizacao, ativo
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    sucesso = 0
    erros = 0
    
    for index, row in df.iterrows():
        try:
            now = datetime.now()
            cursor.execute(insert_query, (
                row['codigo'],
                row['abc'],
                row['tipo'],
                row['saldo_manut'],
                row['provid_compras'],
                row['recebimento_esperado'],
                row['transito_manut'],
                row['stage_manut'],
                row['recepcao_manut'],
                row['pendente_ri'],
                row['pecas_teste_kit'],
                row['pecas_teste'],
                row['fornecedor_reparo'],
                row['laboratorio'],
                row['wr'],
                row['wrcr'],
                row['stage_wr'],
                row['cmm'],
                row['coef_perda'],
                now,  # data_criacao
                now,  # data_atualizacao
                'upload_script',  # usuario_criacao
                'upload_script',  # usuario_atualizacao
                1  # ativo
            ))
            sucesso += 1
            
            # Mostrar progresso a cada 100 registros
            if (sucesso % 100) == 0:
                print(f"   Inseridos: {sucesso}/{len(df)}")
                
        except Exception as e:
            erros += 1
            print(f"❌ Erro ao inserir código {row['codigo']}: {str(e)}")
    
    print(f"\n✅ Inserção concluída!")
    print(f"   Sucesso: {sucesso}")
    print(f"   Erros: {erros}")
    
    return sucesso, erros

def main():
    """Função principal"""
    print("=" * 70)
    print("🚀 UPLOAD DE DADOS CSV PARA AZURE SQL DATABASE")
    print("=" * 70)
    
    # Verificar se o arquivo CSV existe
    if not os.path.exists(CSV_FILE):
        print(f"❌ Arquivo não encontrado: {CSV_FILE}")
        return
    
    try:
        # Ler CSV (delimitador ponto-e-vírgula)
        print(f"\n📂 Lendo arquivo: {CSV_FILE}")
        df = pd.read_csv(CSV_FILE, sep=';', encoding='utf-8')
        print(f"✅ {len(df)} registros encontrados no CSV")
        print(f"✅ Colunas: {', '.join(df.columns.tolist())}")
        
        # Validar dados
        if not validar_dados(df):
            print("\n❌ Validação falhou. Corrija os dados e tente novamente.")
            return
        
        # Preparar dados
        df_prep = preparar_dados(df)
        
        # Conectar ao banco
        print("\n🔌 Conectando ao Azure SQL Database...")
        conn_str = get_connection_string()
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print("✅ Conexão estabelecida!")
        
        # Perguntar se deseja limpar a tabela
        print("\n⚠️  ATENÇÃO: Deseja limpar a tabela antes de inserir os novos dados?")
        resposta = input("   Digite 'SIM' para limpar ou qualquer outra tecla para manter os dados existentes: ")
        
        if resposta.strip().upper() == 'SIM':
            limpar_tabela(cursor)
            conn.commit()
        
        # Inserir dados
        sucesso, erros = inserir_dados(cursor, df_prep)
        
        # Commit
        print("\n💾 Salvando alterações no banco de dados...")
        conn.commit()
        print("✅ Alterações salvas com sucesso!")
        
        # Estatísticas finais
        cursor.execute("SELECT COUNT(*) FROM supply_chain.produtos_estoque WHERE ativo = 1")
        total_registros = cursor.fetchone()[0]
        
        print("\n" + "=" * 70)
        print("📊 ESTATÍSTICAS FINAIS")
        print("=" * 70)
        print(f"Total de registros na tabela: {total_registros}")
        print(f"Registros inseridos agora: {sucesso}")
        if erros > 0:
            print(f"⚠️  Erros durante a inserção: {erros}")
        print("=" * 70)
        
        # Fechar conexão
        cursor.close()
        conn.close()
        print("\n✅ Upload concluído com sucesso!")
        
    except FileNotFoundError:
        print(f"❌ Arquivo CSV não encontrado: {CSV_FILE}")
    except pyodbc.Error as e:
        print(f"❌ Erro de banco de dados: {str(e)}")
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
