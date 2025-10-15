# 📚 Nexum Supply Chain API - Guia Rápido

## 🎯 Acesse a Documentação Interativa

Após iniciar o servidor, acesse:

### 🌐 Swagger UI (Recomendado)
```
http://localhost:5000/docs
```

**O que você pode fazer:**
- ✅ Ver todos os endpoints organizados por categoria
- ✅ Testar cada endpoint diretamente no navegador
- ✅ Ver exemplos de request/response
- ✅ Entender parâmetros e tipos de dados

---

## 🚀 Como Testar

### 1️⃣ Iniciar o Servidor
```bash
# Ativar ambiente virtual
.\NexumEnv\Scripts\Activate.ps1

# Rodar servidor
python app.py
```

### 2️⃣ Acessar Swagger UI
```
http://localhost:5000/docs
```

### 3️⃣ Testar Endpoints

#### 🔐 **Autenticação**

**Login:**
1. Vá em `/api/users/login`
2. Clique em "Try it out"
3. Insira no body:
```json
{
  "email": "admin@nexum.com",
  "senha": "Admin@123"
}
```
4. Clique em "Execute"
5. Veja a resposta com os dados do usuário

**Registrar Novo Usuário:**
1. Vá em `/api/users/register`
2. Insira:
```json
{
  "email": "seu@email.com",
  "senha": "SuaSenha@123",
  "matricula": "MAT001",
  "nivel_acesso": "planejador"
}
```

---

#### 📦 **Produtos**

**Ver Tipos de Materiais:**
- GET `/api/produtos/tipos`
- Mostra os 3 tipos: reparável, testável, descartável

**Listar Produtos:**
- GET `/api/produtos/`
- Query params:
  - `page=1` - Página
  - `per_page=20` - Itens por página
  - `abc=A` - Filtrar por classe A, B ou C
  - `tipo=10` - Filtrar por tipo (10, 19, 20)

**Exemplos de Filtros:**
```
/api/produtos/?abc=A&tipo=10           # Apenas classe A reparáveis
/api/produtos/?tipo=20&page=1&per_page=50  # Descartáveis, 50 por página
```

**Buscar Produto Específico:**
- GET `/api/produtos/<id>` - Por ID
- GET `/api/produtos/codigo/<codigo>` - Por código

---

#### 📊 **Análises e Estatísticas**

**Produtos Críticos:**
```
GET /api/produtos/criticos?limit=10
```
Retorna produtos com estoque zero e CMM > 1

**Estatísticas Gerais:**
```
GET /api/produtos/estatisticas
```
Retorna:
- Total de produtos
- Produtos ativos/inativos
- Distribuição ABC
- CMM médio
- Etc.

---

## 📋 Endpoints Principais

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| **🏠 SISTEMA** |
| GET | `/` | Info da API |
| GET | `/docs` | Swagger UI |
| GET | `/apispec.json` | Spec OpenAPI |
| **🔐 AUTENTICAÇÃO** |
| POST | `/api/users/login` | Login |
| POST | `/api/users/register` | Cadastro |
| GET | `/api/users/` | Listar usuários |
| GET | `/api/users/niveis-acesso` | Níveis disponíveis |
| **📦 PRODUTOS** |
| GET | `/api/produtos/tipos` | Tipos de materiais |
| GET | `/api/produtos/` | Listar (com filtros) |
| GET | `/api/produtos/<id>` | Buscar por ID |
| GET | `/api/produtos/codigo/<codigo>` | Buscar por código |
| POST | `/api/produtos/` | Criar produto |
| PUT | `/api/produtos/<id>` | Atualizar |
| DELETE | `/api/produtos/<id>` | Deletar (soft) |
| **📊 ANÁLISES** |
| GET | `/api/produtos/criticos` | Produtos críticos |
| GET | `/api/produtos/estatisticas` | Estatísticas gerais |

---

## 🧪 Exemplos de Teste Rápido

### Via Swagger UI (Mais Fácil)
1. Acesse `http://localhost:5000/docs`
2. Navegue pelas seções
3. Clique em "Try it out"
4. Preencha os campos
5. Veja a resposta

### Via cURL
```bash
# Login
curl -X POST http://localhost:5000/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@nexum.com","senha":"Admin@123"}'

# Listar produtos classe A
curl "http://localhost:5000/api/produtos/?abc=A"

# Ver tipos
curl http://localhost:5000/api/produtos/tipos

# Estatísticas
curl http://localhost:5000/api/produtos/estatisticas
```

### Via Python
```python
import requests

# Login
response = requests.post('http://localhost:5000/api/users/login', json={
    'email': 'admin@nexum.com',
    'senha': 'Admin@123'
})
print(response.json())

# Listar produtos
produtos = requests.get('http://localhost:5000/api/produtos/?abc=A').json()
print(produtos)
```

---

## 🎨 Recursos do Swagger

- **📱 Try it out**: Teste endpoints direto do navegador
- **📖 Models**: Veja estrutura de dados
- **🔍 Schemas**: Entenda request/response
- **⚡ Execute**: Rode requests em tempo real
- **📋 Copy**: Copie exemplos de cURL/Python

---

## 💡 Dicas

1. **Comece testando o login** para entender a estrutura
2. **Use `/api/produtos/tipos`** para ver informações sobre tipologia
3. **Teste os filtros** para ver a flexibilidade da API
4. **Veja as estatísticas** para entender os dados disponíveis
5. **Explore o Swagger UI** - ele mostra tudo automaticamente!

---

## 🆘 Troubleshooting

**Servidor não inicia?**
- Verifique se o ambiente virtual está ativado
- Confira se todas as dependências estão instaladas: `pip install -r requirements.txt`

**Erro de conexão com banco?**
- Verifique o arquivo `.env` com credenciais Azure SQL
- Teste conexão: `python aux_files/test_connection.py`

**Swagger não carrega?**
- Limpe cache do navegador
- Tente acessar `/apispec.json` primeiro
- Reinicie o servidor

---

**🚀 Pronto! Agora é só acessar http://localhost:5000/docs e explorar!**
