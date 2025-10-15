"""
Controller de Usuário
Responsável pelas rotas da API (endpoints)
"""

from flask import Blueprint, request, jsonify
from api.services import user_service

user_bp = Blueprint('user', __name__, url_prefix='/api/usuarios')


@user_bp.route('/login', methods=['POST'])
def login():
    """
    Endpoint de Login
    
    POST /api/users/login
    Body: {
        "email": "user@example.com",
        "senha": "senha123"
    }
    
    Returns:
        200: Login bem-sucedido (retorna dados do usuário)
        400: Dados inválidos
        401: Credenciais inválidas
    """
    try:
        data = request.get_json()
        
        # Validar dados recebidos
        if not data:
            return jsonify({
                'success': False,
                'message': 'Nenhum dado fornecido'
            }), 400
        
        email = data.get('email')
        senha = data.get('senha')
        
        if not email or not senha:
            return jsonify({
                'success': False,
                'message': 'Email e senha são obrigatórios'
            }), 400
        
        # Tentar autenticar
        user = user_service.login(email, senha)
        
        if user:
            return jsonify({
                'success': True,
                'message': 'Login realizado com sucesso',
                'user': user
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Email ou senha incorretos'
            }), 401
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro no servidor: {str(e)}'
        }), 500


@user_bp.route('/register', methods=['POST'])
def register():
    """
    Endpoint de Registro
    
    POST /api/users/register
    Body: {
        "email": "novo@example.com",
        "senha": "Senha@123",
        "matricula": "MAT001",
        "nivel_acesso": "usuario"  # opcional, padrão: 'usuario'
    }
    
    Returns:
        201: Usuário criado com sucesso
        400: Dados inválidos ou erro de validação
        500: Erro no servidor
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'message': 'Nenhum dado fornecido'
            }), 400
        
        email = data.get('email')
        senha = data.get('senha')
        matricula = data.get('matricula')
        nivel_acesso = data.get('nivel_acesso', 'usuario')
        
        # Validar campos obrigatórios
        if not email or not senha or not matricula:
            return jsonify({
                'success': False,
                'message': 'Email, senha e matrícula são obrigatórios'
            }), 400
        
        # Registrar usuário
        result = user_service.registrar_usuario(email, senha, matricula, nivel_acesso)
        
        if result['success']:
            return jsonify(result), 201
        else:
            return jsonify(result), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro no servidor: {str(e)}'
        }), 500


@user_bp.route('/change-password', methods=['PUT'])
def change_password():
    """
    Endpoint para Alterar Senha
    
    PUT /api/users/change-password
    Body: {
        "user_id": 1,
        "senha_atual": "SenhaAtual@123",
        "nova_senha": "NovaSenha@456"
    }
    
    Returns:
        200: Senha alterada com sucesso
        400: Dados inválidos
        500: Erro no servidor
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'message': 'Nenhum dado fornecido'
            }), 400
        
        user_id = data.get('user_id')
        senha_atual = data.get('senha_atual')
        nova_senha = data.get('nova_senha')
        
        if not user_id or not senha_atual or not nova_senha:
            return jsonify({
                'success': False,
                'message': 'user_id, senha_atual e nova_senha são obrigatórios'
            }), 400
        
        # Alterar senha
        result = user_service.alterar_senha(user_id, senha_atual, nova_senha)
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro no servidor: {str(e)}'
        }), 500


@user_bp.route('/email/<email>', methods=['GET'])
def get_by_email(email):
    """
    Buscar usuário por email
    
    GET /api/users/email/user@example.com
    
    Returns:
        200: Usuário encontrado
        404: Usuário não encontrado
    """
    try:
        user = user_service.buscar_usuario_por_email(email)
        
        if user:
            return jsonify({
                'success': True,
                'user': user
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Usuário não encontrado'
            }), 404
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro no servidor: {str(e)}'
        }), 500


@user_bp.route('/matricula/<matricula>', methods=['GET'])
def get_by_matricula(matricula):
    """
    Buscar usuário por matrícula
    
    GET /api/users/matricula/MAT001
    
    Returns:
        200: Usuário encontrado
        404: Usuário não encontrado
    """
    try:
        user = user_service.buscar_usuario_por_matricula(matricula)
        
        if user:
            return jsonify({
                'success': True,
                'user': user
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Usuário não encontrado'
            }), 404
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro no servidor: {str(e)}'
        }), 500


@user_bp.route('/', methods=['GET'])
def list_users():
    """
    Listar todos os usuários
    
    GET /api/users/
    
    Returns:
        200: Lista de usuários
    """
    try:
        users = user_service.listar_usuarios()
        
        return jsonify({
            'success': True,
            'total': len(users),
            'users': users
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro no servidor: {str(e)}'
        }), 500


@user_bp.route('/niveis-acesso', methods=['GET'])
def get_niveis_acesso():
    """
    Endpoint para obter níveis de acesso disponíveis
    
    GET /api/users/niveis-acesso
    
    Returns:
        200: Lista de níveis de acesso disponíveis
        {
            "success": true,
            "niveis_acesso": ["planejador", "comprador", "fiscal", "gestor"]
        }
    """
    try:
        result = user_service.obter_niveis_acesso()
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Erro no servidor: {str(e)}',
            'niveis_acesso': ['comprador', 'fiscal', 'gestor', 'planejador']  # Fallback
        }), 500