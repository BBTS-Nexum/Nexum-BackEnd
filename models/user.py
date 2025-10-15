"""
Model de Usuário
Representa um usuário do sistema Nexum Supply Chain
"""

class User:
    def __init__(self, id=None, email=None, senha=None, matricula=None, 
                 nivel_acesso=None, data_criacao=None, data_atualizacao=None):
        self.id = id
        self.email = email
        self.senha = senha  # Hash bcrypt
        self.matricula = matricula
        self.nivel_acesso = nivel_acesso
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
    
    def to_dict(self, include_senha=False):
        """Converte o usuário para dicionário (sem senha por padrão)"""
        user_dict = {
            'id': self.id,
            'email': self.email,
            'matricula': self.matricula,
            'nivel_acesso': self.nivel_acesso,
            'data_criacao': str(self.data_criacao) if self.data_criacao else None,
            'data_atualizacao': str(self.data_atualizacao) if self.data_atualizacao else None
        }
        
        if include_senha:
            user_dict['senha'] = self.senha
        
        return user_dict
    
    @staticmethod
    def from_db_row(row):
        """Cria um objeto User a partir de uma linha do banco de dados"""
        if not row:
            return None
        
        return User(
            id=row.id if hasattr(row, 'id') else row[0],
            email=row.email if hasattr(row, 'email') else row[1],
            senha=row.senha if hasattr(row, 'senha') else row[2],
            matricula=row.matricula if hasattr(row, 'matricula') else row[3],
            nivel_acesso=row.nivel_acesso if hasattr(row, 'nivel_acesso') else row[4],
            data_criacao=row.data_criacao if hasattr(row, 'data_criacao') else (row[5] if len(row) > 5 else None),
            data_atualizacao=row.data_atualizacao if hasattr(row, 'data_atualizacao') else (row[6] if len(row) > 6 else None)
        )
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, matricula={self.matricula}, nivel={self.nivel_acesso})>"