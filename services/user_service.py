"""
Service de Usuário
Responsável pela lógica de negócio (validações, bcrypt, etc.)
"""

import bcrypt
import re
from repositories import user_repository


def login(email, senha):
    """
    Autentica um usuário
    
    Args:
        email (str): Email do usuário
        senha (str): Senha em texto plano
    
    Returns:
        dict: Dados do usuário (sem senha) ou None se falhar
    """
    # Validar entrada
    if not email or not senha:
        return None
    
    # Buscar usuário no banco
    user = user_repository.find_by_email(email)
    
    if not user:
        return None
    
    # Verificar senha com bcrypt
    try:
        # A senha no banco já está como string, converter para bytes
        senha_hash_bytes = user.senha.encode('utf-8') if isinstance(user.senha, str) else user.senha
        senha_input_bytes = senha.encode('utf-8')
        
        senha_valida = bcrypt.checkpw(senha_input_bytes, senha_hash_bytes)
        
    except Exception as e:
        print(f"❌ ERRO ao verificar senha: {str(e)}")
        return None
    
    if not senha_valida:
        return None
    
    # Retornar dados do usuário (SEM senha)
    return user.to_dict(include_senha=False)


def registrar_usuario(email, senha, matricula, nivel_acesso='usuario'):
    """
    Registra um novo usuário
    
    Args:
        email (str): Email do usuário
        senha (str): Senha em texto plano
        matricula (str): Matrícula do usuário
        nivel_acesso (str): Nível de acesso (padrão: 'usuario')
    
    Returns:
        dict: {'success': bool, 'message': str, 'user': dict or None}
    """
    # Validar email
    if not validar_email(email):
        return {
            'success': False,
            'message': 'Email inválido',
            'user': None
        }
    
    # Validar senha
    senha_valida, mensagem_senha = validar_senha(senha)
    if not senha_valida:
        return {
            'success': False,
            'message': mensagem_senha,
            'user': None
        }
    
    # Verificar se email já existe
    if user_repository.find_by_email(email):
        return {
            'success': False,
            'message': 'Email já cadastrado',
            'user': None
        }
    
    # Verificar se matrícula já existe
    if user_repository.find_by_matricula(matricula):
        return {
            'success': False,
            'message': 'Matrícula já cadastrada',
            'user': None
        }
    
    # Hash da senha com bcrypt
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Criar usuário no banco
    success, user_id = user_repository.create_user(email, senha_hash, matricula, nivel_acesso)
    
    if not success:
        return {
            'success': False,
            'message': 'Erro ao criar usuário no banco de dados',
            'user': None
        }
    
    # Buscar usuário criado
    user = user_repository.find_by_id(user_id)
    user_dict = user.to_dict(include_senha=False) if user else None
    
    return {
        'success': True,
        'message': 'Usuário criado com sucesso',
        'user': user_dict
    }


def alterar_senha(user_id, senha_atual, nova_senha):
    """
    Altera a senha de um usuário
    
    Args:
        user_id (int): ID do usuário
        senha_atual (str): Senha atual em texto plano
        nova_senha (str): Nova senha em texto plano
    
    Returns:
        dict: {'success': bool, 'message': str}
    """
    # Buscar usuário
    user = user_repository.find_by_id(user_id)
    
    if not user:
        return {
            'success': False,
            'message': 'Usuário não encontrado'
        }
    
    # Verificar senha atual
    senha_atual_valida = bcrypt.checkpw(
        senha_atual.encode('utf-8'),
        user.senha.encode('utf-8')
    )
    
    if not senha_atual_valida:
        return {
            'success': False,
            'message': 'Senha atual incorreta'
        }
    
    # Validar nova senha
    senha_valida, mensagem = validar_senha(nova_senha)
    if not senha_valida:
        return {
            'success': False,
            'message': mensagem
        }
    
    # Hash da nova senha
    nova_senha_hash = bcrypt.hashpw(nova_senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # Atualizar no banco
    success = user_repository.update_senha(user_id, nova_senha_hash)
    
    if success:
        return {
            'success': True,
            'message': 'Senha alterada com sucesso'
        }
    else:
        return {
            'success': False,
            'message': 'Erro ao alterar senha no banco de dados'
        }


def buscar_usuario_por_email(email):
    """
    Busca um usuário por email
    
    Args:
        email (str): Email do usuário
    
    Returns:
        dict: Dados do usuário (sem senha) ou None
    """
    user = user_repository.find_by_email(email)
    return user.to_dict(include_senha=False) if user else None


def buscar_usuario_por_matricula(matricula):
    """
    Busca um usuário por matrícula
    
    Args:
        matricula (str): Matrícula do usuário
    
    Returns:
        dict: Dados do usuário (sem senha) ou None
    """
    user = user_repository.find_by_matricula(matricula)
    return user.to_dict(include_senha=False) if user else None


def listar_usuarios():
    """
    Lista todos os usuários
    
    Returns:
        list: Lista de dicionários com dados dos usuários (sem senha)
    """
    users = user_repository.list_all_users()
    return [user.to_dict(include_senha=False) for user in users]


# ============================================================================
# FUNÇÕES DE VALIDAÇÃO
# ============================================================================

def validar_email(email):
    """
    Valida formato de email
    
    Args:
        email (str): Email a validar
    
    Returns:
        bool: True se válido, False se inválido
    """
    if not email:
        return False
    
    # Regex simples para validar email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validar_senha(senha):
    """
    Valida força da senha
    
    Requisitos:
    - Mínimo 8 caracteres
    - Pelo menos 1 letra maiúscula
    - Pelo menos 1 letra minúscula
    - Pelo menos 1 número
    - Pelo menos 1 caractere especial
    
    Args:
        senha (str): Senha a validar
    
    Returns:
        tuple: (bool: válido, str: mensagem)
    """
    if not senha:
        return False, 'Senha não pode ser vazia'
    
    if len(senha) < 8:
        return False, 'Senha deve ter no mínimo 8 caracteres'
    
    if not re.search(r'[A-Z]', senha):
        return False, 'Senha deve conter pelo menos uma letra maiúscula'
    
    if not re.search(r'[a-z]', senha):
        return False, 'Senha deve conter pelo menos uma letra minúscula'
    
    if not re.search(r'[0-9]', senha):
        return False, 'Senha deve conter pelo menos um número'
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return False, 'Senha deve conter pelo menos um caractere especial (!@#$%^&*...)'
    
    return True, 'Senha válida'


def obter_niveis_acesso():
    """
    Obtém a lista de níveis de acesso disponíveis
    
    Returns:
        dict: {'success': bool, 'niveis_acesso': list}
    """
    try:
        niveis = user_repository.get_niveis_acesso()
        
        return {
            'success': True,
            'niveis_acesso': niveis
        }
    except Exception as e:
        print(f"Erro ao buscar níveis de acesso: {str(e)}")
        # Retorna níveis padrão em caso de erro
        return {
            'success': True,
            'niveis_acesso': ['comprador', 'fiscal', 'gestor', 'planejador']
        }