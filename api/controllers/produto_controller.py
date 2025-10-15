"""
Controller de Produto - Rotas da API
"""
from flask import Blueprint, request, jsonify
import api.services.produto_service as ps

produto_bp = Blueprint('produto', __name__)


@produto_bp.route('/tipos', methods=['GET'])
def get_tipos():
    """
    Retornar tipos de materiais
    ---
    tags:
      - 📦 Produtos
    summary: Lista todos os tipos de materiais disponíveis
    description: |
      Retorna informações sobre os 3 tipos de materiais do sistema:
      - Tipo 10 (Reparável): Peças 100% reparáveis
      - Tipo 19 (Testável): Peças passíveis de teste
      - Tipo 20 (Descartável): Peças de uso único
    responses:
      200:
        description: Lista de tipos com descrição e cálculo de saldo
        schema:
          properties:
            success:
              type: boolean
            tipos:
              type: array
              items:
                type: object
                properties:
                  codigo:
                    type: integer
                  nome:
                    type: string
                  descricao:
                    type: string
                  emoji:
                    type: string
                  calculo_saldo:
                    type: string
    """
    return jsonify({
        'success': True,
        'tipos': [
            {
                'codigo': 10,
                'nome': 'reparavel',
                'descricao': 'Peças 100% reparáveis',
                'emoji': '🔧',
                'calculo_saldo': 'saldo + peças_teste + peças_reparo - perdas'
            },
            {
                'codigo': 19,
                'nome': 'testavel',
                'descricao': 'Peças passíveis de teste',
                'emoji': '🧪',
                'calculo_saldo': 'saldo + peças_teste + peças_reparo - perdas'
            },
            {
                'codigo': 20,
                'nome': 'descartavel',
                'descricao': 'Peças descartadas após consumo',
                'emoji': '🗑️',
                'calculo_saldo': 'apenas saldo (peças boas)'
            }
        ]
    }), 200


@produto_bp.route('/', methods=['POST'])
def create():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': 'Sem dados'}), 400
        
        codigo, abc, tipo = data.get('codigo'), data.get('abc'), data.get('tipo')
        if not all([codigo, abc, tipo is not None]):
            return jsonify({'success': False, 'message': 'Código, ABC e tipo obrigatórios'}), 400
        
        fields = ['saldo_manut', 'provid_compras', 'recebimento_esperado', 'transito_manut', 
                 'stage_manut', 'recepcao_manut', 'pendente_ri', 'pecas_teste_kit', 'pecas_teste', 
                 'fornecedor_reparo', 'laboratorio', 'wr', 'wrcr', 'stage_wr', 'cmm', 'coef_perda', 'usuario']
        
        kwargs = {k: data[k] for k in fields if k in data}
        result = ps.criar_produto(codigo, abc, tipo, **kwargs)
        return jsonify(result), (201 if result['success'] else 400)
    except Exception as e:
        print(f"❌ create: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500


@produto_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    try:
        produto = ps.buscar_produto_por_id(id)
        if produto:
            return jsonify({'success': True, 'produto': produto}), 200
        return jsonify({'success': False, 'message': 'Não encontrado'}), 404
    except Exception as e:
        print(f"❌ get_one: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500


@produto_bp.route('/codigo/<codigo>', methods=['GET'])
def get_by_code(codigo):
    try:
        produto = ps.buscar_produto_por_codigo(codigo)
        if produto:
            return jsonify({'success': True, 'produto': produto}), 200
        return jsonify({'success': False, 'message': 'Não encontrado'}), 404
    except Exception as e:
        print(f"❌ get_by_code: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500


@produto_bp.route('/', methods=['GET'])
def list_all():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 100, type=int)
        abc = request.args.get('abc', None, type=str)
        tipo = request.args.get('tipo', None, type=int)
        
        if page < 1:
            return jsonify({'success': False, 'message': 'Página >= 1'}), 400
        if not (1 <= per_page <= 1000):
            return jsonify({'success': False, 'message': 'per_page entre 1 e 1000'}), 400
        if abc and abc not in ['A', 'B', 'C']:
            return jsonify({'success': False, 'message': 'ABC: A, B ou C'}), 400
        if tipo and tipo not in [10, 19, 20]:
            return jsonify({'success': False, 'message': 'Tipo: 10, 19 ou 20'}), 400
        
        result = ps.listar_produtos(page, per_page, abc, tipo)
        return jsonify({'success': True, **result}), 200
    except Exception as e:
        print(f"❌ list_all: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500


@produto_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'message': 'Sem dados'}), 400
        
        result = ps.atualizar_produto(id, **data)
        status = 200 if result['success'] else (404 if 'não encontrado' in result.get('message', '') else 400)
        return jsonify(result), status
    except Exception as e:
        print(f"❌ update: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500


@produto_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        data = request.get_json() or {}
        usuario = data.get('usuario')
        result = ps.deletar_produto(id, usuario)
        status = 200 if result['success'] else (404 if 'não encontrado' in result.get('message', '') else 400)
        return jsonify(result), status
    except Exception as e:
        print(f"❌ delete: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500


@produto_bp.route('/criticos', methods=['GET'])
def criticos():
    try:
        limit = request.args.get('limit', 100, type=int)
        if not (1 <= limit <= 1000):
            return jsonify({'success': False, 'message': 'limit entre 1 e 1000'}), 400
        
        produtos = ps.obter_produtos_criticos(limit)
        return jsonify({'success': True, 'total': len(produtos), 'produtos': produtos}), 200
    except Exception as e:
        print(f"❌ criticos: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500


@produto_bp.route('/estatisticas', methods=['GET'])
def stats():
    try:
        estat = ps.obter_estatisticas()
        return jsonify({'success': True, 'estatisticas': estat}), 200
    except Exception as e:
        print(f"❌ stats: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500


@produto_bp.route('/<int:id>/indicadores', methods=['GET'])
def indicadores(id):
    """
    GET /api/produtos/{id}/indicadores
    Retorna todos os indicadores calculados para um produto específico
    """
    try:
        result = ps.obter_indicadores_produto(id)
        status = 200 if result['success'] else 404
        return jsonify(result), status
    except Exception as e:
        print(f"❌ indicadores: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500


@produto_bp.route('/necessidade-compra', methods=['GET'])
def necessidade_compra():
    """
    GET /api/produtos/necessidade-compra
    Lista produtos que precisam ser comprados (QA > 0)
    """
    try:
        limit = request.args.get('limit', 100, type=int)
        if not (1 <= limit <= 1000):
            return jsonify({'success': False, 'message': 'limit entre 1 e 1000'}), 400
        
        result = ps.obter_produtos_necessidade_compra(limit)
        return jsonify(result), 200
    except Exception as e:
        print(f"❌ necessidade_compra: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500


@produto_bp.route('/cobertura-baixa', methods=['GET'])
def cobertura_baixa():
    """
    GET /api/produtos/cobertura-baixa
    Lista produtos com cobertura menor que X meses
    """
    try:
        meses = request.args.get('meses', 2, type=float)
        limit = request.args.get('limit', 100, type=int)
        
        if not (1 <= limit <= 1000):
            return jsonify({'success': False, 'message': 'limit entre 1 e 1000'}), 400
        
        if meses < 0:
            return jsonify({'success': False, 'message': 'meses deve ser >= 0'}), 400
        
        result = ps.obter_produtos_cobertura_baixa(meses, limit)
        return jsonify(result), 200
    except Exception as e:
        print(f"❌ cobertura_baixa: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'message': str(e)}), 500

