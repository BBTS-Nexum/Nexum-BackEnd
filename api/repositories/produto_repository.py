"""
Repository de Produto
Responsável por acessar o banco de dados (camada de dados)
"""

from api.models.produto import Produto
import api.aux_files.sql as db


def find_by_id(produto_id):
    """
    Busca um produto por ID
    
    Args:
        produto_id (int): ID do produto
    
    Returns:
        Produto: Objeto Produto ou None se não encontrado
    """
    query = """
        SELECT id, codigo, abc, tipo, saldo_manut, provid_compras, recebimento_esperado,
               transito_manut, stage_manut, recepcao_manut, pendente_ri,
               pecas_teste_kit, pecas_teste, fornecedor_reparo, laboratorio,
               wr, wrcr, stage_wr, cmm, coef_perda,
               data_criacao, data_atualizacao, usuario_criacao, usuario_atualizacao, ativo
        FROM supply_chain.produtos_estoque 
        WHERE id = ? AND ativo = 1
    """
    
    success, row = db.execute_one_fetch(query, (produto_id,))
    
    if not success or row is None:
        return None
    
    return Produto.from_db_row(row)


def find_by_codigo(codigo):
    """
    Busca um produto por código
    
    Args:
        codigo (str): Código do produto
    
    Returns:
        Produto: Objeto Produto ou None se não encontrado
    """
    query = """
        SELECT id, codigo, abc, tipo, saldo_manut, provid_compras, recebimento_esperado,
               transito_manut, stage_manut, recepcao_manut, pendente_ri,
               pecas_teste_kit, pecas_teste, fornecedor_reparo, laboratorio,
               wr, wrcr, stage_wr, cmm, coef_perda,
               data_criacao, data_atualizacao, usuario_criacao, usuario_atualizacao, ativo
        FROM supply_chain.produtos_estoque 
        WHERE codigo = ? AND ativo = 1
    """
    
    success, row = db.execute_one_fetch(query, (codigo,))
    
    if not success or row is None:
        return None
    
    return Produto.from_db_row(row)


def list_all(limit=100, offset=0, abc=None, tipo=None):
    """
    Lista todos os produtos com paginação e filtros
    
    Args:
        limit (int): Número máximo de produtos a retornar
        offset (int): Offset para paginação
        abc (str): Filtro por classificação ABC (opcional)
        tipo (int): Filtro por tipo (opcional)
    
    Returns:
        list: Lista de objetos Produto
    """
    where_clauses = ["ativo = 1"]
    params = []
    
    if abc:
        where_clauses.append("abc = ?")
        params.append(abc)
    
    if tipo:
        where_clauses.append("tipo = ?")
        params.append(tipo)
    
    where_sql = " AND ".join(where_clauses)
    
    query = f"""
        SELECT id, codigo, abc, tipo, saldo_manut, provid_compras, recebimento_esperado,
               transito_manut, stage_manut, recepcao_manut, pendente_ri,
               pecas_teste_kit, pecas_teste, fornecedor_reparo, laboratorio,
               wr, wrcr, stage_wr, cmm, coef_perda,
               data_criacao, data_atualizacao, usuario_criacao, usuario_atualizacao, ativo
        FROM supply_chain.produtos_estoque 
        WHERE {where_sql}
        ORDER BY id
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY
    """
    
    params.extend([offset, limit])
    
    success, rows = db.execute_fetch_all(query, tuple(params))
    
    if not success or not rows:
        return []
    
    return [Produto.from_db_row(row) for row in rows]


def count_all(abc=None, tipo=None):
    """
    Conta o total de produtos com filtros
    
    Args:
        abc (str): Filtro por classificação ABC (opcional)
        tipo (int): Filtro por tipo (opcional)
    
    Returns:
        int: Total de produtos
    """
    where_clauses = ["ativo = 1"]
    params = []
    
    if abc:
        where_clauses.append("abc = ?")
        params.append(abc)
    
    if tipo:
        where_clauses.append("tipo = ?")
        params.append(tipo)
    
    where_sql = " AND ".join(where_clauses)
    
    query = f"""
        SELECT COUNT(*) as total
        FROM supply_chain.produtos_estoque 
        WHERE {where_sql}
    """
    
    success, row = db.execute_one_fetch(query, tuple(params) if params else None)
    
    if not success or not row:
        return 0
    
    return row.total if hasattr(row, 'total') else row[0]


def create_produto(codigo, abc, tipo, saldo_manut=0, provid_compras=0, recebimento_esperado=0,
                   transito_manut=0, stage_manut=0, recepcao_manut=0, pendente_ri=0,
                   pecas_teste_kit=0, pecas_teste=0, fornecedor_reparo=0, laboratorio=0,
                   wr=0, wrcr=0, stage_wr=0, cmm=0.00, coef_perda=0.00000000, usuario=None):
    """
    Cria um novo produto
    
    Args:
        codigo (str): Código único do produto
        abc (str): Classificação ABC (A, B ou C)
        tipo (int): Tipo do produto (10, 19 ou 20)
        ... (outros campos)
        usuario (str): Usuário que está criando
    
    Returns:
        tuple: (success: bool, produto_id: int or None)
    """
    query = """
        INSERT INTO supply_chain.produtos_estoque (
            codigo, abc, tipo, saldo_manut, provid_compras, recebimento_esperado,
            transito_manut, stage_manut, recepcao_manut, pendente_ri,
            pecas_teste_kit, pecas_teste, fornecedor_reparo, laboratorio,
            wr, wrcr, stage_wr, cmm, coef_perda, usuario_criacao, usuario_atualizacao
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    params = (
        codigo, abc, tipo, saldo_manut, provid_compras, recebimento_esperado,
        transito_manut, stage_manut, recepcao_manut, pendente_ri,
        pecas_teste_kit, pecas_teste, fornecedor_reparo, laboratorio,
        wr, wrcr, stage_wr, cmm, coef_perda, usuario, usuario
    )
    
    success = db.execute_commit(query, params)
    
    if not success:
        return False, None
    
    # Buscar o ID do produto recém-criado
    produto = find_by_codigo(codigo)
    return True, produto.id if produto else None


def update_produto(produto_id, **kwargs):
    """
    Atualiza um produto
    
    Args:
        produto_id (int): ID do produto
        **kwargs: Campos a atualizar
    
    Returns:
        bool: True se sucesso, False se erro
    """
    # Campos permitidos para atualização
    allowed_fields = [
        'codigo', 'abc', 'tipo', 'saldo_manut', 'provid_compras', 'recebimento_esperado',
        'transito_manut', 'stage_manut', 'recepcao_manut', 'pendente_ri',
        'pecas_teste_kit', 'pecas_teste', 'fornecedor_reparo', 'laboratorio',
        'wr', 'wrcr', 'stage_wr', 'cmm', 'coef_perda', 'ativo'
    ]
    
    # Filtrar apenas campos permitidos
    updates = {k: v for k, v in kwargs.items() if k in allowed_fields}
    
    if not updates:
        return False
    
    # Construir query dinamicamente
    set_clause = ", ".join([f"{field} = ?" for field in updates.keys()])
    set_clause += ", data_atualizacao = GETDATE()"
    
    # Adicionar usuario_atualizacao se fornecido
    if 'usuario' in kwargs:
        set_clause += ", usuario_atualizacao = ?"
        params = list(updates.values()) + [kwargs['usuario'], produto_id]
    else:
        params = list(updates.values()) + [produto_id]
    
    query = f"""
        UPDATE supply_chain.produtos_estoque 
        SET {set_clause}
        WHERE id = ? AND ativo = 1
    """
    
    return db.execute_commit(query, tuple(params))


def delete_produto(produto_id, usuario=None):
    """
    Deleta um produto (soft delete - marca como inativo)
    
    Args:
        produto_id (int): ID do produto
        usuario (str): Usuário que está deletando
    
    Returns:
        bool: True se sucesso, False se erro
    """
    query = """
        UPDATE supply_chain.produtos_estoque 
        SET ativo = 0, 
            data_atualizacao = GETDATE(),
            usuario_atualizacao = ?
        WHERE id = ? AND ativo = 1
    """
    
    return db.execute_commit(query, (usuario or 'SYSTEM', produto_id))


def get_produtos_criticos(limit=100):
    """
    Busca produtos críticos (CMM alto, estoque baixo)
    
    Args:
        limit (int): Número máximo de produtos
    
    Returns:
        list: Lista de objetos Produto
    """
    query = """
        SELECT TOP (?) 
               id, codigo, abc, tipo, saldo_manut, provid_compras, recebimento_esperado,
               transito_manut, stage_manut, recepcao_manut, pendente_ri,
               pecas_teste_kit, pecas_teste, fornecedor_reparo, laboratorio,
               wr, wrcr, stage_wr, cmm, coef_perda,
               data_criacao, data_atualizacao, usuario_criacao, usuario_atualizacao, ativo
        FROM supply_chain.produtos_estoque 
        WHERE ativo = 1 AND saldo_manut = 0 AND cmm > 1
        ORDER BY cmm DESC
    """
    
    success, rows = db.execute_fetch_all(query, (limit,))
    
    if not success or not rows:
        return []
    
    return [Produto.from_db_row(row) for row in rows]


def get_estatisticas():
    """
    Retorna estatísticas gerais dos produtos
    
    Returns:
        dict: Estatísticas
    """
    query = """
        SELECT 
            COUNT(*) as total_produtos,
            SUM(CASE WHEN saldo_manut = 0 THEN 1 ELSE 0 END) as sem_estoque,
            SUM(CASE WHEN saldo_manut > 0 THEN 1 ELSE 0 END) as com_estoque,
            SUM(CASE WHEN abc = 'A' THEN 1 ELSE 0 END) as classificacao_a,
            SUM(CASE WHEN abc = 'B' THEN 1 ELSE 0 END) as classificacao_b,
            SUM(CASE WHEN abc = 'C' THEN 1 ELSE 0 END) as classificacao_c,
            SUM(saldo_manut) as estoque_total,
            AVG(cmm) as cmm_medio,
            SUM(CASE WHEN saldo_manut = 0 AND cmm > 1 THEN 1 ELSE 0 END) as produtos_criticos
        FROM supply_chain.produtos_estoque 
        WHERE ativo = 1
    """
    
    success, row = db.execute_one_fetch(query)
    
    if not success or not row:
        return {}
    
    return {
        'total_produtos': row.total_produtos if hasattr(row, 'total_produtos') else row[0],
        'sem_estoque': row.sem_estoque if hasattr(row, 'sem_estoque') else row[1],
        'com_estoque': row.com_estoque if hasattr(row, 'com_estoque') else row[2],
        'classificacao_a': row.classificacao_a if hasattr(row, 'classificacao_a') else row[3],
        'classificacao_b': row.classificacao_b if hasattr(row, 'classificacao_b') else row[4],
        'classificacao_c': row.classificacao_c if hasattr(row, 'classificacao_c') else row[5],
        'estoque_total': row.estoque_total if hasattr(row, 'estoque_total') else row[6],
        'cmm_medio': float(row.cmm_medio) if hasattr(row, 'cmm_medio') and row.cmm_medio else 0.00,
        'produtos_criticos': row.produtos_criticos if hasattr(row, 'produtos_criticos') else row[8]
    }
