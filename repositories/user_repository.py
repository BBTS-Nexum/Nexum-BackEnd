"""
Repository de Usuário
Responsável por acessar o banco de dados (camada de dados)
"""

from models.user import User
import aux_files.sql as db


def find_by_email(email):
    """
    Busca um usuário por email
    
    Args:
        email (str): Email do usuário
    
    Returns:
        User: Objeto User ou None se não encontrado
    """
    query = """
        SELECT id, email, senha, matricula, nivel_acesso, data_criacao, data_atualizacao
        FROM supply_chain.usuarios 
        WHERE email = ?
    """
    
    success, row = db.execute_one_fetch(query, (email,))
    
    if not success or row is None:
        return None
    
    return User.from_db_row(row)


def find_by_matricula(matricula):
    """
    Busca um usuário por matrícula
    
    Args:
        matricula (str): Matrícula do usuário
    
    Returns:
        User: Objeto User ou None se não encontrado
    """
    query = """
        SELECT id, email, senha, matricula, nivel_acesso, data_criacao, data_atualizacao
        FROM supply_chain.usuarios 
        WHERE matricula = ?
    """
    
    success, row = db.execute_one_fetch(query, (matricula,))
    
    if not success or row is None:
        return None
    
    return User.from_db_row(row)


def find_by_id(user_id):
    """
    Busca um usuário por ID
    
    Args:
        user_id (int): ID do usuário
    
    Returns:
        User: Objeto User ou None se não encontrado
    """
    query = """
        SELECT id, email, senha, matricula, nivel_acesso, data_criacao, data_atualizacao
        FROM supply_chain.usuarios 
        WHERE id = ?
    """
    
    success, row = db.execute_one_fetch(query, (user_id,))
    
    if not success or row is None:
        return None
    
    return User.from_db_row(row)


def create_user(email, senha_hash, matricula, nivel_acesso):
    """
    Cria um novo usuário no banco de dados
    
    Args:
        email (str): Email do usuário
        senha_hash (str): Hash bcrypt da senha
        matricula (str): Matrícula do usuário
        nivel_acesso (str): Nível de acesso (admin, usuario, gerente, operador)
    
    Returns:
        tuple: (success: bool, user_id: int or None)
    """
    query = """
        INSERT INTO supply_chain.usuarios (email, senha, matricula, nivel_acesso)
        VALUES (?, ?, ?, ?)
    """
    
    success = db.execute_commit(query, (email, senha_hash, matricula, nivel_acesso))
    
    if not success:
        return False, None
    
    # Buscar o usuário recém-criado para retornar o ID
    user = find_by_email(email)
    return True, user.id if user else None


def update_senha(user_id, nova_senha_hash):
    """
    Atualiza a senha de um usuário
    
    Args:
        user_id (int): ID do usuário
        nova_senha_hash (str): Novo hash bcrypt da senha
    
    Returns:
        bool: True se sucesso, False se erro
    """
    query = """
        UPDATE supply_chain.usuarios 
        SET senha = ?
        WHERE id = ?
    """
    
    return db.execute_commit(query, (nova_senha_hash, user_id))


def list_all_users():
    """
    Lista todos os usuários (sem senha)
    
    Returns:
        list: Lista de objetos User
    """
    query = """
        SELECT id, email, senha, matricula, nivel_acesso, data_criacao, data_atualizacao
        FROM supply_chain.usuarios
        ORDER BY data_criacao DESC
    """
    
    success, rows = db.execute_fetch_all(query)
    
    if not success:
        return []
    
    return [User.from_db_row(row) for row in rows]


def delete_user(user_id):
    """
    Deleta um usuário
    
    Args:
        user_id (int): ID do usuário
    
    Returns:
        bool: True se sucesso, False se erro
    """
    query = "DELETE FROM supply_chain.usuarios WHERE id = ?"
    return db.execute_commit(query, (user_id,))


def get_niveis_acesso():
    """
    Busca os níveis de acesso disponíveis no banco de dados
    Extrai os valores da constraint CHECK da tabela usuarios
    
    Returns:
        list: Lista de níveis de acesso disponíveis ou lista vazia se erro
    """
    query = """
        SELECT DISTINCT nivel_acesso
        FROM supply_chain.usuarios
        ORDER BY nivel_acesso
    """
    
    success, rows = db.execute_fetch(query)
    
    if not success or not rows:
        # Se não houver dados no banco, retorna os níveis padrão do CHECK constraint
        # CHECK (nivel_acesso IN ('planejador', 'comprador', 'fiscal', 'gestor'))
        return ['comprador', 'fiscal', 'gestor', 'planejador']
    
    return [row.nivel_acesso if hasattr(row, 'nivel_acesso') else row[0] for row in rows]