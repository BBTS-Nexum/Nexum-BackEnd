"""
Script para gerar o hash bcrypt correto para a senha Admin@123
"""

import bcrypt


def gerar_hash():
    """
    Gera o hash bcrypt para a senha Admin@123
    """
    senha = "Admin@123"
    
    print("=" * 70)
    print("GERADOR DE HASH BCRYPT")
    print("=" * 70)
    print()
    print(f"Senha em texto: {senha}")
    print()
    
    # Gerar hash
    hash_gerado = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    hash_str = hash_gerado.decode('utf-8')
    
    print(f"Hash gerado: {hash_str}")
    print(f"Tamanho: {len(hash_str)} caracteres")
    print()
    
    # Verificar se o hash funciona
    valido = bcrypt.checkpw(senha.encode('utf-8'), hash_gerado)
    print(f"Verificação: {'✅ VÁLIDO' if valido else '❌ INVÁLIDO'}")
    print()
    
    # Gerar UPDATE SQL
    print("=" * 70)
    print("SQL PARA ATUALIZAR O HASH NO BANCO:")
    print("=" * 70)
    print()
    print(f"UPDATE supply_chain.usuarios")
    print(f"SET senha = '{hash_str}'")
    print(f"WHERE email = 'admin@nexum.com';")
    print()
    
    return hash_str


if __name__ == "__main__":
    gerar_hash()
