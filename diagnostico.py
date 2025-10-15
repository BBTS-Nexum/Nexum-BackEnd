"""
Script de diagnóstico para verificar endpoint de produtos
"""

import requests
import json

API_URL = "http://localhost:5000"

def test_api_status():
    """Testa se a API está online"""
    print("\n" + "="*60)
    print("1. TESTANDO STATUS DA API")
    print("="*60)
    
    try:
        response = requests.get(f"{API_URL}/")
        print(f"✅ Status: {response.status_code}")
        print(f"📦 Resposta: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        return True
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def test_produtos_endpoint():
    """Testa endpoint de produtos"""
    print("\n" + "="*60)
    print("2. TESTANDO ENDPOINT DE PRODUTOS")
    print("="*60)
    
    try:
        url = f"{API_URL}/api/produtos/?page=1&per_page=10"
        print(f"🔗 URL: {url}")
        
        response = requests.get(url)
        print(f"📡 Status Code: {response.status_code}")
        
        data = response.json()
        print(f"📦 Response Keys: {list(data.keys())}")
        
        if data.get('success'):
            print(f"✅ Success: True")
            print(f"📊 Total: {data.get('total', 0)}")
            print(f"📄 Página: {data.get('page', 0)}")
            print(f"📄 Total Páginas: {data.get('pages', 0)}")
            print(f"🔢 Produtos Retornados: {len(data.get('produtos', []))}")
            
            if data.get('produtos'):
                print(f"\n📦 Primeiro Produto:")
                print(json.dumps(data['produtos'][0], indent=2, ensure_ascii=False))
        else:
            print(f"❌ Error: {data.get('message')}")
            
        return data.get('success', False)
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_produtos_criticos():
    """Testa endpoint de produtos críticos"""
    print("\n" + "="*60)
    print("3. TESTANDO PRODUTOS CRÍTICOS")
    print("="*60)
    
    try:
        response = requests.get(f"{API_URL}/api/produtos/criticos?limit=5")
        print(f"📡 Status: {response.status_code}")
        
        data = response.json()
        if data.get('success'):
            print(f"✅ Produtos críticos: {data.get('total', 0)}")
        else:
            print(f"❌ Erro: {data.get('message')}")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

def test_estatisticas():
    """Testa endpoint de estatísticas"""
    print("\n" + "="*60)
    print("4. TESTANDO ESTATÍSTICAS")
    print("="*60)
    
    try:
        response = requests.get(f"{API_URL}/api/produtos/estatisticas")
        print(f"📡 Status: {response.status_code}")
        
        data = response.json()
        if data.get('success'):
            stats = data.get('estatisticas', {})
            print(f"✅ Estatísticas:")
            print(f"   - Total Produtos: {stats.get('total_produtos', 0)}")
            print(f"   - Produtos Ativos: {stats.get('produtos_ativos', 0)}")
            print(f"   - Produtos Críticos: {stats.get('produtos_criticos', 0)}")
            print(f"   - CMM Médio: {stats.get('cmm_medio', 0)}")
        else:
            print(f"❌ Erro: {data.get('message')}")
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🔍 DIAGNÓSTICO DO SISTEMA NEXUM")
    print("="*60)
    
    # Testa API
    if not test_api_status():
        print("\n❌ API não está respondendo!")
        print("👉 Execute: python app.py")
        exit(1)
    
    # Testa endpoints
    test_produtos_endpoint()
    test_produtos_criticos()
    test_estatisticas()
    
    print("\n" + "="*60)
    print("✅ DIAGNÓSTICO CONCLUÍDO")
    print("="*60 + "\n")
