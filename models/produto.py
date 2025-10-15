"""
Model de Produto
Representa um produto do sistema Nexum Supply Chain

Tipos de Material:
- reparavel (T-10): Peças 100% reparáveis
- testavel (T-19): Peças passíveis de teste
- descartavel (T-20): Peças descartadas após consumo
"""

# Mapeamento de tipos
TIPO_MAP = {
    10: 'reparavel',
    19: 'testavel',
    20: 'descartavel'
}

TIPO_REVERSE_MAP = {
    'reparavel': 10,
    'testavel': 19,
    'descartavel': 20
}

class Produto:
    def __init__(self, id=None, codigo=None, abc=None, tipo=None, 
                 saldo_manut=0, provid_compras=0, recebimento_esperado=0,
                 transito_manut=0, stage_manut=0, recepcao_manut=0, pendente_ri=0,
                 pecas_teste_kit=0, pecas_teste=0, fornecedor_reparo=0, laboratorio=0,
                 wr=0, wrcr=0, stage_wr=0, cmm=0.00, coef_perda=0.00000000,
                 data_criacao=None, data_atualizacao=None, 
                 usuario_criacao=None, usuario_atualizacao=None, ativo=True):
        self.id = id
        self.codigo = codigo
        self.abc = abc
        self.tipo = tipo
        self.saldo_manut = saldo_manut
        self.provid_compras = provid_compras
        self.recebimento_esperado = recebimento_esperado
        self.transito_manut = transito_manut
        self.stage_manut = stage_manut
        self.recepcao_manut = recepcao_manut
        self.pendente_ri = pendente_ri
        self.pecas_teste_kit = pecas_teste_kit
        self.pecas_teste = pecas_teste
        self.fornecedor_reparo = fornecedor_reparo
        self.laboratorio = laboratorio
        self.wr = wr
        self.wrcr = wrcr
        self.stage_wr = stage_wr
        self.cmm = cmm
        self.coef_perda = coef_perda
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.usuario_criacao = usuario_criacao
        self.usuario_atualizacao = usuario_atualizacao
        self.ativo = ativo
    
    def calcular_saldo_total(self):
        """
        Calcula o saldo total baseado no tipo do material
        
        - Tipo 10 (reparavel): saldo + peças em teste + peças para reparo - perdas
        - Tipo 19 (testavel): saldo + peças em teste + peças para reparo - perdas  
        - Tipo 20 (descartavel): apenas saldo (peças boas)
        """
        if self.tipo == 20:  # descartavel
            return self.saldo_manut or 0
        
        # reparavel (10) ou testavel (19)
        pecas_boas = self.saldo_manut or 0
        pecas_teste = (self.pecas_teste_kit or 0) + (self.pecas_teste or 0)
        pecas_reparo = (self.fornecedor_reparo or 0) + (self.laboratorio or 0) + (self.wr or 0)
        
        # Aplicar coeficiente de perda
        coef = self.coef_perda or 0
        perda_estimada = pecas_reparo * coef if coef > 0 else 0
        
        saldo_total = pecas_boas + pecas_teste + pecas_reparo - perda_estimada
        return max(0, saldo_total)  # Não pode ser negativo
    
    def to_dict(self):
        """Converte o produto para dicionário"""
        return {
            'id': self.id,
            'codigo': self.codigo,
            'abc': self.abc,
            'tipo': self.tipo,
            'tipo_nome': TIPO_MAP.get(self.tipo, 'desconhecido'),
            'saldo_manut': self.saldo_manut,
            'provid_compras': self.provid_compras,
            'recebimento_esperado': self.recebimento_esperado,
            'transito_manut': self.transito_manut,
            'stage_manut': self.stage_manut,
            'recepcao_manut': self.recepcao_manut,
            'pendente_ri': self.pendente_ri,
            'pecas_teste_kit': self.pecas_teste_kit,
            'pecas_teste': self.pecas_teste,
            'fornecedor_reparo': self.fornecedor_reparo,
            'laboratorio': self.laboratorio,
            'wr': self.wr,
            'wrcr': self.wrcr,
            'stage_wr': self.stage_wr,
            'cmm': float(self.cmm) if self.cmm else 0.00,
            'coef_perda': float(self.coef_perda) if self.coef_perda else 0.00000000,
            'saldo_total': self.calcular_saldo_total(),
            'data_criacao': str(self.data_criacao) if self.data_criacao else None,
            'data_atualizacao': str(self.data_atualizacao) if self.data_atualizacao else None,
            'usuario_criacao': self.usuario_criacao,
            'usuario_atualizacao': self.usuario_atualizacao,
            'ativo': self.ativo
        }
    
    @staticmethod
    def from_db_row(row):
        """Cria um objeto Produto a partir de uma linha do banco de dados"""
        if not row:
            return None
        
        return Produto(
            id=row.id if hasattr(row, 'id') else row[0],
            codigo=row.codigo if hasattr(row, 'codigo') else row[1],
            abc=row.abc if hasattr(row, 'abc') else row[2],
            tipo=row.tipo if hasattr(row, 'tipo') else row[3],
            saldo_manut=row.saldo_manut if hasattr(row, 'saldo_manut') else row[4],
            provid_compras=row.provid_compras if hasattr(row, 'provid_compras') else row[5],
            recebimento_esperado=row.recebimento_esperado if hasattr(row, 'recebimento_esperado') else row[6],
            transito_manut=row.transito_manut if hasattr(row, 'transito_manut') else row[7],
            stage_manut=row.stage_manut if hasattr(row, 'stage_manut') else row[8],
            recepcao_manut=row.recepcao_manut if hasattr(row, 'recepcao_manut') else row[9],
            pendente_ri=row.pendente_ri if hasattr(row, 'pendente_ri') else row[10],
            pecas_teste_kit=row.pecas_teste_kit if hasattr(row, 'pecas_teste_kit') else row[11],
            pecas_teste=row.pecas_teste if hasattr(row, 'pecas_teste') else row[12],
            fornecedor_reparo=row.fornecedor_reparo if hasattr(row, 'fornecedor_reparo') else row[13],
            laboratorio=row.laboratorio if hasattr(row, 'laboratorio') else row[14],
            wr=row.wr if hasattr(row, 'wr') else row[15],
            wrcr=row.wrcr if hasattr(row, 'wrcr') else row[16],
            stage_wr=row.stage_wr if hasattr(row, 'stage_wr') else row[17],
            cmm=row.cmm if hasattr(row, 'cmm') else row[18],
            coef_perda=row.coef_perda if hasattr(row, 'coef_perda') else row[19],
            data_criacao=row.data_criacao if hasattr(row, 'data_criacao') else (row[20] if len(row) > 20 else None),
            data_atualizacao=row.data_atualizacao if hasattr(row, 'data_atualizacao') else (row[21] if len(row) > 21 else None),
            usuario_criacao=row.usuario_criacao if hasattr(row, 'usuario_criacao') else (row[22] if len(row) > 22 else None),
            usuario_atualizacao=row.usuario_atualizacao if hasattr(row, 'usuario_atualizacao') else (row[23] if len(row) > 23 else None),
            ativo=row.ativo if hasattr(row, 'ativo') else (row[24] if len(row) > 24 else True)
        )
    
    def __repr__(self):
        return f"<Produto(id={self.id}, codigo={self.codigo}, abc={self.abc}, tipo={self.tipo}, estoque={self.saldo_manut})>"
