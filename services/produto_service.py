"""
Service de Produto
Responsável pela lógica de negócio (validações, transformações, etc.)
"""

from repositories import produto_repository


def criar_produto(codigo, abc, tipo, **kwargs):
    """
    Cria um novo produto com validações
    
    Args:
        codigo (str): Código único do produto
        abc (str): Classificação ABC (A, B ou C)
        tipo (int): Tipo do produto (10, 19 ou 20)
        **kwargs: Outros campos opcionais
    
    Returns:
        dict: {'success': bool, 'message': str, 'produto': dict or None}
    """
    # Validar código
    if not codigo or len(codigo.strip()) == 0:
        return {
            'success': False,
            'message': 'Código do produto é obrigatório',
            'produto': None
        }
    
    # Validar ABC
    if abc not in ['A', 'B', 'C']:
        return {
            'success': False,
            'message': 'Classificação ABC deve ser A, B ou C',
            'produto': None
        }
    
    # Validar tipo
    if tipo not in [10, 19, 20]:
        return {
            'success': False,
            'message': 'Tipo deve ser 10, 19 ou 20',
            'produto': None
        }
    
    # Verificar se código já existe
    produto_existente = produto_repository.find_by_codigo(codigo)
    if produto_existente:
        return {
            'success': False,
            'message': 'Código de produto já cadastrado',
            'produto': None
        }
    
    # Validar campos numéricos (devem ser >= 0)
    campos_numericos = [
        'saldo_manut', 'provid_compras', 'recebimento_esperado',
        'transito_manut', 'stage_manut', 'recepcao_manut', 'pendente_ri',
        'pecas_teste_kit', 'pecas_teste', 'fornecedor_reparo', 'laboratorio',
        'wr', 'wrcr', 'stage_wr'
    ]
    
    for campo in campos_numericos:
        if campo in kwargs and kwargs[campo] is not None:
            try:
                valor = int(kwargs[campo])
                if valor < 0:
                    return {
                        'success': False,
                        'message': f'{campo} não pode ser negativo',
                        'produto': None
                    }
                kwargs[campo] = valor
            except (ValueError, TypeError):
                return {
                    'success': False,
                    'message': f'{campo} deve ser um número inteiro',
                    'produto': None
                }
    
    # Validar CMM e coef_perda
    if 'cmm' in kwargs and kwargs['cmm'] is not None:
        try:
            cmm = float(kwargs['cmm'])
            if cmm < 0:
                return {
                    'success': False,
                    'message': 'CMM não pode ser negativo',
                    'produto': None
                }
            kwargs['cmm'] = cmm
        except (ValueError, TypeError):
            return {
                'success': False,
                'message': 'CMM deve ser um número decimal',
                'produto': None
            }
    
    if 'coef_perda' in kwargs and kwargs['coef_perda'] is not None:
        try:
            coef_perda = float(kwargs['coef_perda'])
            if coef_perda < 0:
                return {
                    'success': False,
                    'message': 'Coeficiente de perda não pode ser negativo',
                    'produto': None
                }
            kwargs['coef_perda'] = coef_perda
        except (ValueError, TypeError):
            return {
                'success': False,
                'message': 'Coeficiente de perda deve ser um número decimal',
                'produto': None
            }
    
    # Criar produto no banco
    success, produto_id = produto_repository.create_produto(codigo, abc, tipo, **kwargs)
    
    if not success:
        return {
            'success': False,
            'message': 'Erro ao criar produto no banco de dados',
            'produto': None
        }
    
    # Buscar produto criado
    produto = produto_repository.find_by_id(produto_id)
    
    return {
        'success': True,
        'message': 'Produto criado com sucesso',
        'produto': produto.to_dict() if produto else None
    }


def buscar_produto_por_id(produto_id):
    """
    Busca produto por ID
    
    Args:
        produto_id (int): ID do produto
    
    Returns:
        dict or None: Dados do produto ou None
    """
    produto = produto_repository.find_by_id(produto_id)
    return produto.to_dict() if produto else None


def buscar_produto_por_codigo(codigo):
    """
    Busca produto por código
    
    Args:
        codigo (str): Código do produto
    
    Returns:
        dict or None: Dados do produto ou None
    """
    produto = produto_repository.find_by_codigo(codigo)
    return produto.to_dict() if produto else None


def listar_produtos(page=1, per_page=100, abc=None, tipo=None):
    """
    Lista produtos com paginação e filtros
    
    Args:
        page (int): Número da página (começa em 1)
        per_page (int): Itens por página
        abc (str): Filtro por classificação ABC
        tipo (int): Filtro por tipo
    
    Returns:
        dict: Lista de produtos e metadados de paginação
    """
    offset = (page - 1) * per_page
    
    produtos = produto_repository.list_all(limit=per_page, offset=offset, abc=abc, tipo=tipo)
    total = produto_repository.count_all(abc=abc, tipo=tipo)
    
    return {
        'produtos': [p.to_dict() for p in produtos],
        'page': page,
        'per_page': per_page,
        'total': total,
        'total_pages': (total + per_page - 1) // per_page  # Ceiling division
    }


def atualizar_produto(produto_id, **kwargs):
    """
    Atualiza um produto
    
    Args:
        produto_id (int): ID do produto
        **kwargs: Campos a atualizar
    
    Returns:
        dict: {'success': bool, 'message': str, 'produto': dict or None}
    """
    # Verificar se produto existe
    produto_existente = produto_repository.find_by_id(produto_id)
    if not produto_existente:
        return {
            'success': False,
            'message': 'Produto não encontrado',
            'produto': None
        }
    
    # Validar ABC se fornecido
    if 'abc' in kwargs and kwargs['abc'] not in ['A', 'B', 'C']:
        return {
            'success': False,
            'message': 'Classificação ABC deve ser A, B ou C',
            'produto': None
        }
    
    # Validar tipo se fornecido
    if 'tipo' in kwargs and kwargs['tipo'] not in [10, 19, 20]:
        return {
            'success': False,
            'message': 'Tipo deve ser 10, 19 ou 20',
            'produto': None
        }
    
    # Validar código se fornecido (deve ser único)
    if 'codigo' in kwargs:
        outro_produto = produto_repository.find_by_codigo(kwargs['codigo'])
        if outro_produto and outro_produto.id != produto_id:
            return {
                'success': False,
                'message': 'Código já está em uso por outro produto',
                'produto': None
            }
    
    # Validar campos numéricos
    campos_numericos = [
        'saldo_manut', 'provid_compras', 'recebimento_esperado',
        'transito_manut', 'stage_manut', 'recepcao_manut', 'pendente_ri',
        'pecas_teste_kit', 'pecas_teste', 'fornecedor_reparo', 'laboratorio',
        'wr', 'wrcr', 'stage_wr'
    ]
    
    for campo in campos_numericos:
        if campo in kwargs and kwargs[campo] is not None:
            try:
                valor = int(kwargs[campo])
                if valor < 0:
                    return {
                        'success': False,
                        'message': f'{campo} não pode ser negativo',
                        'produto': None
                    }
                kwargs[campo] = valor
            except (ValueError, TypeError):
                return {
                    'success': False,
                    'message': f'{campo} deve ser um número inteiro',
                    'produto': None
                }
    
    # Validar CMM e coef_perda
    if 'cmm' in kwargs and kwargs['cmm'] is not None:
        try:
            kwargs['cmm'] = float(kwargs['cmm'])
            if kwargs['cmm'] < 0:
                return {
                    'success': False,
                    'message': 'CMM não pode ser negativo',
                    'produto': None
                }
        except (ValueError, TypeError):
            return {
                'success': False,
                'message': 'CMM deve ser um número decimal',
                'produto': None
            }
    
    if 'coef_perda' in kwargs and kwargs['coef_perda'] is not None:
        try:
            kwargs['coef_perda'] = float(kwargs['coef_perda'])
            if kwargs['coef_perda'] < 0:
                return {
                    'success': False,
                    'message': 'Coeficiente de perda não pode ser negativo',
                    'produto': None
                }
        except (ValueError, TypeError):
            return {
                'success': False,
                'message': 'Coeficiente de perda deve ser um número decimal',
                'produto': None
            }
    
    # Atualizar produto
    success = produto_repository.update_produto(produto_id, **kwargs)
    
    if not success:
        return {
            'success': False,
            'message': 'Erro ao atualizar produto no banco de dados',
            'produto': None
        }
    
    # Buscar produto atualizado
    produto = produto_repository.find_by_id(produto_id)
    
    return {
        'success': True,
        'message': 'Produto atualizado com sucesso',
        'produto': produto.to_dict() if produto else None
    }


def deletar_produto(produto_id, usuario=None):
    """
    Deleta um produto (soft delete)
    
    Args:
        produto_id (int): ID do produto
        usuario (str): Usuário que está deletando
    
    Returns:
        dict: {'success': bool, 'message': str}
    """
    # Verificar se produto existe
    produto = produto_repository.find_by_id(produto_id)
    if not produto:
        return {
            'success': False,
            'message': 'Produto não encontrado'
        }
    
    # Deletar produto
    success = produto_repository.delete_produto(produto_id, usuario)
    
    if not success:
        return {
            'success': False,
            'message': 'Erro ao deletar produto'
        }
    
    return {
        'success': True,
        'message': 'Produto deletado com sucesso'
    }


def obter_produtos_criticos(limit=100):
    """
    Obtém produtos críticos (CMM alto, estoque baixo)
    
    Args:
        limit (int): Número máximo de produtos
    
    Returns:
        list: Lista de produtos críticos
    """
    produtos = produto_repository.get_produtos_criticos(limit)
    return [p.to_dict() for p in produtos]


def obter_estatisticas():
    """
    Obtém estatísticas gerais dos produtos
    
    Returns:
        dict: Estatísticas
    """
    return produto_repository.get_estatisticas()


def obter_indicadores_produto(produto_id):
    """
    Retorna todos os indicadores calculados para um produto
    
    Args:
        produto_id (int): ID do produto
    
    Returns:
        dict: {'success': bool, 'produto': dict com indicadores}
    """
    produto = produto_repository.find_by_id(produto_id)
    
    if not produto:
        return {
            'success': False,
            'message': 'Produto não encontrado'
        }
    
    return {
        'success': True,
        'produto': produto.to_dict(incluir_indicadores=True)
    }


def obter_produtos_necessidade_compra(limit=100):
    """
    Lista produtos que precisam ser comprados (QA > 0)
    
    Args:
        limit (int): Número máximo de produtos
    
    Returns:
        dict: {'success': bool, 'total': int, 'produtos': list}
    """
    produtos = produto_repository.list_all(page=1, per_page=5000)['produtos']
    
    produtos_compra = []
    for p in produtos:
        qa = p.calcular_quantidade_adquirir()
        if qa > 0:
            produto_dict = p.to_dict(incluir_indicadores=True)
            produtos_compra.append(produto_dict)
    
    # Ordenar por QA decrescente (maior necessidade primeiro)
    produtos_compra.sort(key=lambda x: x['indicadores']['quantidade_adquirir'], reverse=True)
    
    # Limitar resultado
    produtos_compra = produtos_compra[:limit]
    
    return {
        'success': True,
        'total': len(produtos_compra),
        'produtos': produtos_compra
    }


def obter_produtos_cobertura_baixa(meses=2, limit=100):
    """
    Lista produtos com cobertura menor que X meses
    
    Args:
        meses (float): Número de meses de cobertura mínima
        limit (int): Número máximo de produtos
    
    Returns:
        dict: {'success': bool, 'total': int, 'produtos': list}
    """
    produtos = produto_repository.list_all(page=1, per_page=5000)['produtos']
    
    produtos_baixa = []
    for p in produtos:
        cobertura = p.calcular_cobertura_meses()
        if cobertura < meses and p.cmm > 0:  # Apenas se tiver CMM > 0
            produto_dict = p.to_dict(incluir_indicadores=True)
            produtos_baixa.append(produto_dict)
    
    # Ordenar por cobertura crescente (menor cobertura primeiro)
    produtos_baixa.sort(key=lambda x: x['indicadores']['cobertura_meses'])
    
    # Limitar resultado
    produtos_baixa = produtos_baixa[:limit]
    
    return {
        'success': True,
        'total': len(produtos_baixa),
        'produtos': produtos_baixa
    }

