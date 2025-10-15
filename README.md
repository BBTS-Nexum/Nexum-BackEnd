# 📦 Nexum Supply Chain - Backend API# 📦 Nexum Supply Chain - Backend API



> Sistema completo de gerenciamento de cadeia de suprimentos com autenticação segura, rastreabilidade em tempo real e API REST robusta.> Sistema completo de gerenciamento de cadeia de suprimentos com autenticação segura, rastreabilidade em tempo real e API REST robusta.



[![Azure](https://img.shields.io/badge/Azure-SQL_Database-0078D4?logo=microsoftazure)](https://azure.microsoft.com)[![Azure](https://img.shields.io/badge/Azure-SQL_Database-0078D4?logo=microsoftazure)](https://azure.microsoft.com)

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)](https://www.python.org)[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)](https://www.python.org)

[![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?logo=flask)](https://flask.palletsprojects.com)[![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?logo=flask)](https://flask.palletsprojects.com)

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)



------



## 📑 Índice## 📑 Índice



- [Visão Geral](#-visão-geral)- [Visão Geral](#-visão-geral)

- [Quick Start](#-quick-start)- [Quick Start](#-quick-start)

- [Estrutura do Projeto](#-estrutura-do-projeto)- [Estrutura do Projeto](#-estrutura-do-projeto)

- [Configuração do Ambiente](#️-configuração-do-ambiente)- [Configuração do Ambiente](#-configuração-do-ambiente)

- [Banco de Dados](#️-banco-de-dados)- [Banco de Dados](#-banco-de-dados)

- [Sistema de Autenticação](#-sistema-de-autenticação)- [Sistema de Autenticação](#-sistema-de-autenticação)

- [API Endpoints](#-api-endpoints)- [API Endpoints](#-api-endpoints)

- [Interface de Testes](#-interface-de-testes)- [Testes](#-testes)

- [Arquitetura](#️-arquitetura)- [Arquitetura](#-arquitetura)

- [Troubleshooting](#-troubleshooting)- [Deployment](#-deployment)

- [Troubleshooting](#-troubleshooting)

---


## 🎯 Visão Geral


O **Nexum Supply Chain Backend** é uma API REST construída com Flask que oferece:

O **Nexum Supply Chain Backend** é uma API REST construída com Flask que oferece:

- 🔐 **Autenticação Segura**: Sistema completo de login com bcrypt e validações robustas

- 📊 **Gestão de Usuários**: CRUD completo com diferentes níveis de acesso- 🔐 **Autenticação Segura**: Sistema completo de login com bcrypt e validações robustas

- 🔄 **Níveis Dinâmicos**: Carregamento automático de níveis de acesso do banco- 📊 **Gestão de Usuários**: CRUD completo com diferentes níveis de acesso

- 🛡️ **Segurança**: Senhas hasheadas, validações de email e senha forte- 🔄 **Níveis Dinâmicos**: Carregamento automático de níveis de acesso do banco

- 📈 **Rastreabilidade**: Logs detalhados de todas as operações- 🛡️ **Segurança**: Senhas hasheadas, validações de email e senha forte

- 🎨 **Interface de Testes**: HTML/JS para testar endpoints facilmente- 📈 **Rastreabilidade**: Logs detalhados de todas as operações

- 🎨 **Interface de Testes**: HTML/JS para testar endpoints facilmente

### ✨ Funcionalidades Principais

- ✅ Login e cadastro de usuários

- ✅ Alteração de senha com validação- ✅ Login e cadastro de usuários

- ✅ Busca de usuários por email, matrícula ou ID- ✅ Alteração de senha com validação

- ✅ Listagem de todos os usuários- ✅ Busca de usuários por email, matrícula ou ID

- ✅ Níveis de acesso dinâmicos (planejador, comprador, fiscal, gestor)- ✅ Listagem de todos os usuários

- ✅ CORS habilitado para integração com frontend- ✅ Níveis de acesso dinâmicos (planejador, comprador, fiscal, gestor)

- ✅ Validações robustas de entrada- ✅ CORS habilitado para integração com frontend

- ✅ Tratamento de erros adequado- ✅ Validações robustas de entrada

- ✅ Tratamento de erros adequado

---

## 🚀 Quick Start

### **1. Clone o Repositório**

```bash### **1. Clone o Repositório**

git clone https://github.com/BBTS-Nexum/Nexum-BackEnd.git```bash

cd Nexum-BackEndgit clone https://github.com/BBTS-Nexum/Nexum-BackEnd.git

```cd Nexum-BackEnd

```

### **2. Crie o Ambiente Virtual**

```bash### **2. Crie o Ambiente Virtual**

# Windows PowerShell```bash

python -m venv NexumEnv# Windows PowerShell

.\NexumEnv\Scripts\Activate.ps1python -m venv NexumEnv

.\NexumEnv\Scripts\Activate.ps1

# Linux/Mac

python3 -m venv NexumEnv# Linux/Mac

source NexumEnv/bin/activatepython3 -m venv NexumEnv

```source NexumEnv/bin/activate

```

### **3. Instale as Dependências**

```bash### **3. Instale as Dependências**

pip install -r requirements.txt```bash

```pip install -r requirements.txt

```

### **4. Configure o Banco de Dados**

### **4. Configure o Banco de Dados**

Crie o arquivo `.env` com suas credenciais do Azure:

Crie o arquivo `.env` com suas credenciais do Azure:

```bash

# Copie o exemplo```bash

Copy-Item .env.example .env# Copie o exemplo

Copy-Item .env.example .env

# Edite com suas credenciais

notepad .env# Edite com suas credenciais

```notepad .env

```

Preencha o `.env`:

```envPreencha o `.env`:

AZURE_SQL_DRIVER=ODBC Driver 18 for SQL Server```env

AZURE_SQL_SERVER=seu-servidor.database.windows.netAZURE_SQL_DRIVER=ODBC Driver 18 for SQL Server

AZURE_SQL_PORT=1433AZURE_SQL_SERVER=seu-servidor.database.windows.net

AZURE_SQL_DATABASE=stefanini_appAZURE_SQL_PORT=1433

AZURE_SQL_USERNAME=seu-usuarioAZURE_SQL_DATABASE=seu-database

AZURE_SQL_PASSWORD=sua-senhaAZURE_SQL_USERNAME=seu-usuario

AZURE_SQL_ENCRYPT=yesAZURE_SQL_PASSWORD=sua-senha

AZURE_SQL_TRUST_SERVER_CERTIFICATE=noAZURE_SQL_ENCRYPT=yes

AZURE_SQL_CONNECTION_TIMEOUT=30AZURE_SQL_TRUST_SERVER_CERTIFICATE=no

```AZURE_SQL_CONNECTION_TIMEOUT=30

```

### **5. Execute os Scripts SQL**

### **5. Execute os Scripts SQL**

No Azure Data Studio, execute na ordem:

1. `database/create_users_table.sql` - Cria tabela de usuáriosNo Azure Data Studio, execute na ordem:

2. `database/create_table.sql` - Cria tabela de produtos (opcional)1. `database/create_users_table.sql` - Cria tabela de usuários

2. `database/create_table.sql` - Cria tabela de produtos (opcional)

### **6. Inicie o Servidor**

```bash### **6. Inicie o Servidor**

python app.py```bash

```python app.py

```

✅ Servidor rodando em: **http://localhost:5000**

✅ Servidor rodando em: http://localhost:5000

### **7. Teste a API**

Abra o arquivo de testes no navegador:

```bashAbra o arquivo de testes no navegador:

# Abre interface de testes```bash

.\abrir_teste.bat# Abre interface de testes

.\abrir_teste.bat

# Ou abra manualmente

start test_login.html# Ou abra manualmente

```start test_login.html

```

---

## 📁 Estrutura do Projeto


```

Nexum-BackEnd/```

│Nexum-BackEnd/

├── app.py                      # 🚀 Aplicação Flask principal│

├── requirements.txt            # 📦 Dependências Python├── app.py                      # Aplicação Flask principal

├── .env                        # 🔐 Configurações (não commitado)├── requirements.txt            # Dependências Python

├── .env.example               # 📄 Exemplo de configurações├── .env                        # Configurações (não commitado)

│├── .env.example               # Exemplo de configurações

├── models/                    # 🎯 Modelos de dados│

│   └── user.py               #    └─ Classe User├── models/                    # Modelos de dados

││   └── user.py               # Classe User

├── repositories/             # 🗄️ Camada de acesso a dados│

│   └── user_repository.py   #    └─ Queries SQL para usuários├── repositories/             # Camada de acesso a dados

││   └── user_repository.py   # Queries SQL para usuários

├── services/                # ⚙️ Lógica de negócio│

│   └── user_service.py     #    └─ Validações e bcrypt├── services/                # Lógica de negócio

││   └── user_service.py     # Validações e bcrypt

├── controllers/            # 🎮 Rotas da API│

│   └── user_controller.py #    └─ Endpoints REST├── controllers/            # Rotas da API

││   └── user_controller.py # Endpoints REST

├── database/              # 💾 Scripts SQL│

│   ├── create_users_table.sql├── database/              # Scripts SQL

│   ├── create_table.sql│   ├── create_users_table.sql

│   └── README.md│   ├── create_table.sql

││   └── README.md

├── aux_files/            # 🛠️ Utilitários│

│   ├── sql.py           #    ├─ Helper de conexão├── aux_files/            # Utilitários

│   ├── test_connection.py  # └─ Teste de conexão│   ├── sql.py           # Helper de conexão

│   └── analise_dados.py    #    └─ Análise de dados│   ├── test_connection.py

││   └── analise_dados.py

├── test_login.html      # 🧪 Interface de testes│

├── test_login.js        # 📝 Lógica de testes├── test_login.html      # Interface de testes

├── test_api.py         # 🤖 Testes automatizados├── test_login.js        # Lógica de testes

├── debug_login.py      # 🐛 Debug de login├── test_api.py         # Testes automatizados

├── gerar_hash.py       # 🔒 Utilitário para gerar hash├── debug_login.py      # Debug de login

├── abrir_teste.bat     # ⚡ Script para abrir testes├── gerar_hash.py       # Utilitário para gerar hash

││

└── NexumEnv/          # 🐍 Ambiente virtual (não commitado)└── NexumEnv/          # Ambiente virtual (não commitado)

``````



------



## ⚙️ Configuração do Ambiente## ⚙️ Configuração do Ambiente



### 📋 Variáveis de Ambiente (.env)### Variáveis de Ambiente (.env)



O sistema usa um arquivo `.env` para configurações sensíveis:O sistema usa um arquivo `.env` para configurações sensíveis:



```env```env

# Azure SQL Database# Azure SQL Database

AZURE_SQL_DRIVER=ODBC Driver 18 for SQL ServerAZURE_SQL_DRIVER=ODBC Driver 18 for SQL Server

AZURE_SQL_SERVER=nexum-server.database.windows.netAZURE_SQL_SERVER=nexum-server.database.windows.net

AZURE_SQL_PORT=1433AZURE_SQL_PORT=1433

AZURE_SQL_DATABASE=stefanini_appAZURE_SQL_DATABASE=stefanini_app

AZURE_SQL_USERNAME=nexumadminAZURE_SQL_USERNAME=nexumadmin

AZURE_SQL_PASSWORD=SuaSenhaSegura123!AZURE_SQL_PASSWORD=SuaSenhaSegura123!

AZURE_SQL_ENCRYPT=yesAZURE_SQL_ENCRYPT=yes

AZURE_SQL_TRUST_SERVER_CERTIFICATE=noAZURE_SQL_TRUST_SERVER_CERTIFICATE=no

AZURE_SQL_CONNECTION_TIMEOUT=30AZURE_SQL_CONNECTION_TIMEOUT=30

``````



### 🔑 Obter Credenciais do Azure### Obter Credenciais do Azure



1. Acesse https://portal.azure.com1. Acesse https://portal.azure.com

2. Navegue até seu **SQL Database**2. Navegue até seu SQL Database

3. Clique em **"Connection strings"**3. Clique em **"Connection strings"**

4. Copie a string **ODBC**4. Copie a string **ODBC**

5. Extraia os valores para o `.env`5. Extraia os valores para o `.env`



**Exemplo de connection string do Azure:**### Configurar Firewall do Azure

```

Driver={ODBC Driver 18 for SQL Server};⚠️ **IMPORTANTE**: Adicione seu IP ao firewall!

Server=tcp:nexum-server.database.windows.net,1433;

Database=stefanini_app;1. No Azure Portal, vá ao **SQL Server** (não Database)

Uid=nexumadmin;2. Menu lateral → **"Networking"**

Pwd={your_password_here};3. Clique **"Add client IP"**

Encrypt=yes;4. Ative **"Allow Azure services..."**

```5. Clique **"Save"**



**Como preencher o .env:**### Dependências Principais

- `AZURE_SQL_SERVER`: nexum-server.database.windows.net (sem `tcp:` e sem `,1433`)

- `AZURE_SQL_DATABASE`: stefanini_app```

- `AZURE_SQL_USERNAME`: nexumadminFlask==3.1.2           # Framework web

- `AZURE_SQL_PASSWORD`: Sua senha realflask-cors==6.0.1      # CORS support

bcrypt==4.1.2          # Hash de senhas

### 🔥 Configurar Firewall do Azurepyodbc==5.2.0          # Conexão SQL Server

python-dotenv==1.0.1   # Variáveis de ambiente

⚠️ **MUITO IMPORTANTE**: O Azure bloqueia todas as conexões por padrão!flasgger==0.9.7.1      # Documentação Swagger (futuro)

```

1. No Azure Portal, vá ao **SQL Server** (não o Database)

2. Menu lateral → **"Networking"** ou **"Firewalls and virtual networks"**---

3. Clique **"Add client IP"** (adiciona seu IP automaticamente)

4. Ative **"Allow Azure services and resources to access this server"**## 🗄️ Banco de Dados

5. Clique **"Save"**

### Tabela: `supply_chain.usuarios`

### 📦 Dependências Principais

```sql

```txtCREATE TABLE supply_chain.usuarios (

Flask==3.1.2           # Framework web    id INT IDENTITY(1,1) PRIMARY KEY,

flask-cors==6.0.1      # CORS support    email NVARCHAR(255) NOT NULL UNIQUE,

bcrypt==4.1.2          # Hash de senhas    senha VARCHAR(255) NOT NULL,          -- Hash bcrypt

pyodbc==5.2.0          # Conexão SQL Server    matricula NVARCHAR(50) NOT NULL UNIQUE,

python-dotenv==1.0.1   # Variáveis de ambiente    nivel_acesso NVARCHAR(50) NOT NULL,   

pytest==8.4.0          # Testes    data_criacao DATETIME2 NOT NULL DEFAULT GETDATE(),

coverage==7.11.0       # Cobertura de testes    data_atualizacao DATETIME2 NOT NULL DEFAULT GETDATE(),

```    

    CONSTRAINT CK_usuarios_nivel_acesso 

---        CHECK (nivel_acesso IN ('planejador', 'comprador', 'fiscal', 'gestor')),

    CONSTRAINT CK_usuarios_email_valido 

## 🗄️ Banco de Dados        CHECK (email LIKE '%_@__%.__%')

)

### 📊 Tabela: `supply_chain.usuarios````



```sql### Níveis de Acesso

CREATE TABLE supply_chain.usuarios (

    id INT IDENTITY(1,1) PRIMARY KEY,- **planejador**: Planejador de Supply Chain

    email NVARCHAR(255) NOT NULL UNIQUE,- **comprador**: Responsável por compras

    senha VARCHAR(255) NOT NULL,          -- Hash bcrypt- **fiscal**: Fiscal de contratos

    matricula NVARCHAR(50) NOT NULL UNIQUE,- **gestor**: Gestor/Administrador

    nivel_acesso NVARCHAR(50) NOT NULL,   

    data_criacao DATETIME2 NOT NULL DEFAULT GETDATE(),### Índices

    data_atualizacao DATETIME2 NOT NULL DEFAULT GETDATE(),

    ```sql

    CONSTRAINT CK_usuarios_nivel_acesso -- Performance em login

        CHECK (nivel_acesso IN ('planejador', 'comprador', 'fiscal', 'gestor')),CREATE NONCLUSTERED INDEX IX_usuarios_email 

    CONSTRAINT CK_usuarios_email_valido     ON supply_chain.usuarios(email)

        CHECK (email LIKE '%_@__%.__%')

)-- Performance em busca por matrícula  

```CREATE NONCLUSTERED INDEX IX_usuarios_matricula 

    ON supply_chain.usuarios(matricula)

### 👥 Níveis de Acesso

-- Performance em filtro por nível

| Nível | Descrição | Permissões |CREATE NONCLUSTERED INDEX IX_usuarios_nivel_acesso 

|-------|-----------|------------|    ON supply_chain.usuarios(nivel_acesso)

| **planejador** | Planejador de Supply Chain | Visualização e análise de dados |```

| **comprador** | Responsável por compras | Gestão de pedidos e fornecedores |

| **fiscal** | Fiscal de contratos | Auditoria e conformidade |---

| **gestor** | Gestor/Administrador | Acesso total ao sistema |

## 🔐 Sistema de Autenticação

### 📈 Índices para Performance

---

```sql

-- Performance em login## 📁 Estrutura do Projeto

CREATE NONCLUSTERED INDEX IX_usuarios_email 

    ON supply_chain.usuarios(email)```

Nexum-BackEnd/

-- Performance em busca por matrícula  ├── app.py                      # Aplicação principal Flask

CREATE NONCLUSTERED INDEX IX_usuarios_matricula ├── analise_dados.py            # Script de análise de dados

    ON supply_chain.usuarios(matricula)├── requirements.txt            # Dependências Python

├── .env.example                # Template de configuração

-- Performance em filtro por nível├── .gitignore                  # Arquivos ignorados pelo Git

CREATE NONCLUSTERED INDEX IX_usuarios_nivel_acesso │

    ON supply_chain.usuarios(nivel_acesso)├── database/                   # Scripts e docs do banco de dados

```│   ├── create_table.sql        # Criação de tabelas, views, SPs

│   ├── insert_data.py          # Script Python para inserção

---│   ├── generate_inserts.py     # Gerador de INSERTs SQL

│   ├── insert_data.sql         # INSERTs gerados (não commitado)

## 🔐 Sistema de Autenticação│   └── README.md               # Documentação do banco

│

### 🏗️ Arquitetura em Camadas├── dados_hackathon.csv         # Dados de entrada (5.000 produtos)

├── SETUP_DATABASE.md           # Guia de setup do banco

```└── README.md                   # Este arquivo

┌─────────────────────────────────────────────────────────────┐```

│                    CLIENT (Frontend/Postman)                │

└──────────────────────┬──────────────────────────────────────┘---

                       │ HTTP Request (JSON)

                       ▼## 🗄️ Banco de Dados

┌─────────────────────────────────────────────────────────────┐

│              CONTROLLER (controllers/user_controller.py)     │### **Tabela Principal**

│  • Recebe requisições HTTP                                   │`supply_chain.produtos_estoque` - Controle completo de estoque

│  • Valida dados de entrada                                   │

│  • Retorna respostas JSON                                    │### **Views Disponíveis**

└──────────────────────┬──────────────────────────────────────┘1. `vw_produtos_criticos` - Produtos com risco de ruptura

                       │ Chama Service2. `vw_dashboard_executivo` - KPIs gerenciais

                       ▼3. `vw_analise_abc` - Análise por classificação

┌─────────────────────────────────────────────────────────────┐

│               SERVICE (services/user_service.py)             │### **Stored Procedures**

│  • Validações de negócio                                     │1. `sp_calcular_necessidade_compra` - Cálculo inteligente de compras

│  • Hash de senha (bcrypt)                                    │

│  • Lógica de autenticação                                    │### **Queries Úteis**

└──────────────────────┬──────────────────────────────────────┘

                       │ Chama Repository```sql

                       ▼-- Ver produtos críticos

┌─────────────────────────────────────────────────────────────┐SELECT * FROM supply_chain.vw_produtos_criticos

│          REPOSITORY (repositories/user_repository.py)        │WHERE nivel_criticidade = 'CRÍTICO';

│  • Queries SQL                                               │

│  • CRUD no banco de dados                                    │-- Calcular necessidade de compra (30 dias, fator 1.5)

│  • Conversão User ↔ Database                                 │EXEC supply_chain.sp_calcular_necessidade_compra 

└──────────────────────┬──────────────────────────────────────┘  @lead_time_dias = 30,

                       │ PyODBC  @fator_seguranca = 1.5;

                       ▼

┌─────────────────────────────────────────────────────────────┐-- Dashboard executivo

│              DATABASE (Azure SQL - supply_chain.usuarios)    │SELECT * FROM supply_chain.vw_dashboard_executivo;

└─────────────────────────────────────────────────────────────┘```

```

📖 **Documentação completa:** [database/README.md](database/README.md)

### 🔒 Segurança

---

#### Hash de Senhas (bcrypt)

## 🔧 Tecnologias

```python

import bcrypt### **Backend**

- **Python 3.11+**

# Ao cadastrar- **Flask 3.1.2** - Framework web

senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())- **PyODBC** - Conexão com Azure SQL

- **Pandas & NumPy** - Análise de dados

# Ao fazer login

senha_valida = bcrypt.checkpw(senha.encode('utf-8'), hash_armazenado.encode('utf-8'))### **Database**

```- **Azure SQL Database** - Banco de dados em nuvem

- **T-SQL** - Stored Procedures e Views

#### Validações de Senha Forte

### **Azure Services (Planejado)**

- ✅ Mínimo 8 caracteres- **Azure Service Bus** - Mensageria

- ✅ Pelo menos 1 letra maiúscula- **Azure Functions** - Serverless computing

- ✅ Pelo menos 1 letra minúscula- **Azure Blob Storage** - Armazenamento de arquivos

- ✅ Pelo menos 1 número- **Azure SignalR** - Comunicação em tempo real

- ✅ Pelo menos 1 caractere especial (!@#$%^&*...)- **Azure Container Apps** - Deploy e hosting



#### Validações de Email---



- ✅ Formato válido (regex)## 🎯 Funcionalidades

- ✅ Constraint no banco de dados

- ✅ Unicidade garantida### ✅ **Implementado**

- [x] Análise completa de dados CSV

### 🔄 Fluxo de Autenticação- [x] Estrutura de banco de dados otimizada

- [x] Views para dashboards

#### Login- [x] Stored procedure para cálculo de compras

- [x] Script de importação de dados

```- [x] Documentação completa

1. Frontend envia: POST /api/users/login

   { "email": "user@email.com", "senha": "senha123" }### 🚧 **Em Desenvolvimento**

- [ ] API REST completa (FastAPI)

2. Controller valida dados e chama Service- [ ] Autenticação com Azure AD B2C

- [ ] Sistema de rastreabilidade

3. Service busca usuário no Repository- [ ] Integração com Azure Service Bus

- [ ] Notificações inteligentes

4. Repository retorna objeto User- [ ] Dashboard web

- [ ] App mobile para scanning

5. Service verifica senha com bcrypt

### 📋 **Planejado**

6. Se válido: retorna dados do usuário (SEM senha)- [ ] Machine Learning para previsão de demanda

   Se inválido: retorna erro 401- [ ] Integração com Power BI

- [ ] Geração automática de relatórios

7. Frontend recebe:- [ ] API de rastreamento com QR Code

   { "success": true, "user": {...} }- [ ] Sistema de workflows (Azure Logic Apps)

```

---

#### Cadastro

## 📈 KPIs e Métricas

```

1. Frontend envia: POST /api/users/registerO sistema calcula automaticamente:

   { "email": "novo@email.com", "senha": "Senha@123", 

     "matricula": "MAT001", "nivel_acesso": "usuario" }| Métrica | Descrição |

|---------|-----------|

2. Controller valida dados obrigatórios| **Taxa de Ruptura** | % de produtos sem estoque |

| **Produtos Críticos** | Itens com alta demanda sem estoque |

3. Service executa validações:| **Necessidade de Compra** | Quantidade a ser comprada por produto |

   - Email válido e único| **Giro de Estoque** | Velocidade de movimentação |

   - Senha forte| **CMM (Consumo Médio Mensal)** | Criticidade do produto |

   - Matrícula única| **Tempo em Trânsito** | Duração média de movimentação |



4. Service gera hash bcrypt da senha---



5. Repository cria usuário no banco## 🔐 Segurança



6. Service busca usuário criado- ✅ Variáveis de ambiente para credenciais

- ✅ `.env` no .gitignore

7. Frontend recebe:- ✅ Conexão criptografada com Azure SQL

   { "success": true, "user": {...} }- ✅ Trigger de auditoria automático

```- 🚧 Azure AD B2C (em desenvolvimento)

- 🚧 Azure Key Vault (planejado)

---

---

## 📡 API Endpoints

## 🤝 Contribuindo

### 📍 Endpoints Disponíveis

1. Fork o projeto

#### **Status da API**2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`

```http3. Commit suas mudanças: `git commit -m 'Add: nova funcionalidade'`

GET /4. Push para a branch: `git push origin feature/nova-funcionalidade`

```5. Abra um Pull Request

Retorna status e versão da API

---

**Response (200 OK):**

```json## 📝 Licença

{

  "success": true,Este projeto está sob a licença especificada no arquivo [LICENSE](LICENSE).

  "message": "Nexum Supply Chain API está online!",

  "version": "1.0.0",---

  "endpoints": {

    "users": "/api/users/",## 👥 Equipe

    "login": "/api/users/login",

    "register": "/api/users/register"**BBTS Nexum Team**

  }- GitHub: [@BBTS-Nexum](https://github.com/BBTS-Nexum)

}

```---



---## 📞 Suporte



#### **Login**- 📧 Email: [criar email do projeto]

```http- 📚 Wiki: [Em breve]

POST /api/users/login- 🐛 Issues: [GitHub Issues](https://github.com/BBTS-Nexum/Nexum-BackEnd/issues)

```

---

**Request Body:**

```json## 🎓 Recursos e Documentação

{

  "email": "usuario@exemplo.com",- [Azure SQL Database Docs](https://docs.microsoft.com/en-us/azure/azure-sql/)

  "senha": "SenhaSegura@123"- [Flask Documentation](https://flask.palletsprojects.com/)

}- [Python Best Practices](https://docs.python-guide.org/)

```- [Supply Chain Management Concepts](https://www.investopedia.com/terms/s/scm.asp)



**Response (200 OK):**---

```json

{<div align="center">

  "success": true,

  "message": "Login realizado com sucesso",**Desenvolvido com ❤️ pela equipe BBTS Nexum**

  "user": {

    "id": 1,⭐ **Se este projeto te ajudou, deixe uma estrela!** ⭐

    "email": "usuario@exemplo.com",

    "matricula": "MAT001",</div>

    "nivel_acesso": "planejador",
    "data_criacao": "2025-10-15 10:30:00",
    "data_atualizacao": "2025-10-15 10:30:00"
  }
}
```

**Response (401 Unauthorized):**
```json
{
  "success": false,
  "message": "Email ou senha incorretos"
}
```

---

#### **Cadastro**
```http
POST /api/users/register
```

**Request Body:**
```json
{
  "email": "novo@exemplo.com",
  "senha": "SenhaForte@456",
  "matricula": "MAT002",
  "nivel_acesso": "comprador"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Usuário criado com sucesso",
  "user": {
    "id": 2,
    "email": "novo@exemplo.com",
    "matricula": "MAT002",
    "nivel_acesso": "comprador",
    "data_criacao": "2025-10-15 11:00:00",
    "data_atualizacao": "2025-10-15 11:00:00"
  }
}
```

**Response (400 Bad Request):**
```json
{
  "success": false,
  "message": "Email já cadastrado"
}
```

---

#### **Alterar Senha**
```http
PUT /api/users/change-password
```

**Request Body:**
```json
{
  "user_id": 1,
  "senha_atual": "SenhaAtual@123",
  "nova_senha": "NovaSenha@456"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Senha alterada com sucesso"
}
```

---

#### **Buscar por Email**
```http
GET /api/users/email/<email>
```

**Exemplo:**
```http
GET /api/users/email/usuario@exemplo.com
```

**Response (200 OK):**
```json
{
  "success": true,
  "user": {
    "id": 1,
    "email": "usuario@exemplo.com",
    "matricula": "MAT001",
    "nivel_acesso": "planejador",
    "data_criacao": "2025-10-15 10:30:00",
    "data_atualizacao": "2025-10-15 10:30:00"
  }
}
```

---

#### **Buscar por Matrícula**
```http
GET /api/users/matricula/<matricula>
```

**Exemplo:**
```http
GET /api/users/matricula/MAT001
```

---

#### **Listar Todos os Usuários**
```http
GET /api/users/
```

**Response (200 OK):**
```json
{
  "success": true,
  "total": 5,
  "users": [
    {
      "id": 1,
      "email": "user1@exemplo.com",
      "matricula": "MAT001",
      "nivel_acesso": "gestor",
      "data_criacao": "2025-10-15 10:00:00",
      "data_atualizacao": "2025-10-15 10:00:00"
    }
  ]
}
```

---

#### **Obter Níveis de Acesso Disponíveis** 🆕
```http
GET /api/users/niveis-acesso
```

**Response (200 OK):**
```json
{
  "success": true,
  "niveis_acesso": ["comprador", "fiscal", "gestor", "planejador"]
}
```

> 💡 **Novidade**: Este endpoint busca dinamicamente os níveis de acesso do banco de dados, permitindo que o frontend sempre esteja atualizado com os níveis disponíveis.

---

## 📦 Endpoints de Produtos

### Gestão de Estoque e Produtos

#### **Criar Produto**
```http
POST /api/produtos/
```

**Request Body:**
```json
{
  "codigo": "PROD001",
  "abc": "A",
  "tipo": 10,
  "saldo_manut": 100,
  "provid_compras": 50,
  "recebimento_esperado": 25,
  "transito_manut": 10,
  "stage_manut": 5,
  "recepcao_manut": 3,
  "pendente_ri": 2,
  "pecas_teste_kit": 0,
  "pecas_teste": 0,
  "fornecedor_reparo": 0,
  "laboratorio": 0,
  "wr": 0,
  "wrcr": 0,
  "stage_wr": 0,
  "cmm": 15.5,
  "coef_perda": 0.05,
  "usuario": "admin@exemplo.com"
}
```

**Validações:**
- `codigo`: Obrigatório, único
- `abc`: Obrigatório, valores aceitos: `"A"`, `"B"`, `"C"`
- `tipo`: Obrigatório, valores aceitos: `10`, `19`, `20`
- Todos os campos numéricos devem ser `>= 0`
- `cmm` e `coef_perda` devem ser `>= 0`

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Produto criado com sucesso",
  "produto": {
    "id": 1,
    "codigo": "PROD001",
    "abc": "A",
    "tipo": 10,
    "saldo_manut": 100,
    "cmm": 15.5,
    "coef_perda": 0.05,
    "data_criacao": "2025-10-15 14:30:00",
    "ativo": true
  }
}
```

---

#### **Buscar Produto por ID**
```http
GET /api/produtos/<id>
```

**Exemplo:**
```http
GET /api/produtos/1
```

**Response (200 OK):**
```json
{
  "success": true,
  "produto": {
    "id": 1,
    "codigo": "PROD001",
    "abc": "A",
    "tipo": 10,
    "saldo_manut": 100,
    "provid_compras": 50,
    "cmm": 15.5,
    "coef_perda": 0.05,
    "data_criacao": "2025-10-15 14:30:00",
    "ativo": true
  }
}
```

---

#### **Buscar Produto por Código**
```http
GET /api/produtos/codigo/<codigo>
```

**Exemplo:**
```http
GET /api/produtos/codigo/PROD001
```

**Response (200 OK):**
```json
{
  "success": true,
  "produto": {
    "id": 1,
    "codigo": "PROD001",
    "abc": "A",
    "tipo": 10,
    "saldo_manut": 100
  }
}
```

---

#### **Listar Produtos (com Paginação e Filtros)**
```http
GET /api/produtos/?page=1&per_page=100&abc=A&tipo=10
```

**Query Parameters:**
- `page` (int): Número da página (padrão: `1`)
- `per_page` (int): Itens por página (padrão: `100`, máx: `1000`)
- `abc` (str): Filtro por classificação ABC (`A`, `B` ou `C`)
- `tipo` (int): Filtro por tipo (`10`, `19` ou `20`)

**Exemplo:**
```http
GET /api/produtos/?page=1&per_page=50&abc=A
```

**Response (200 OK):**
```json
{
  "success": true,
  "produtos": [
    {
      "id": 1,
      "codigo": "PROD001",
      "abc": "A",
      "tipo": 10,
      "saldo_manut": 100
    },
    {
      "id": 2,
      "codigo": "PROD002",
      "abc": "A",
      "tipo": 19,
      "saldo_manut": 75
    }
  ],
  "total": 245,
  "page": 1,
  "per_page": 50,
  "pages": 5
}
```

---

#### **Atualizar Produto**
```http
PUT /api/produtos/<id>
```

**Request Body (campos opcionais):**
```json
{
  "saldo_manut": 150,
  "cmm": 20.0,
  "abc": "B",
  "usuario": "gestor@exemplo.com"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Produto atualizado com sucesso",
  "produto": {
    "id": 1,
    "codigo": "PROD001",
    "abc": "B",
    "saldo_manut": 150,
    "cmm": 20.0,
    "data_atualizacao": "2025-10-15 15:00:00"
  }
}
```

---

#### **Deletar Produto (Soft Delete)**
```http
DELETE /api/produtos/<id>
```

**Request Body (opcional):**
```json
{
  "usuario": "admin@exemplo.com"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Produto deletado com sucesso"
}
```

> 💡 **Soft Delete**: O produto não é removido fisicamente do banco de dados, apenas marcado como inativo (`ativo = 0`).

---

#### **Produtos Críticos**
```http
GET /api/produtos/criticos?limit=100
```

Retorna produtos com **estoque zero** e **CMM alto** (alta demanda).

**Query Parameters:**
- `limit` (int): Número máximo de produtos (padrão: `100`, máx: `1000`)

**Response (200 OK):**
```json
{
  "success": true,
  "total": 15,
  "produtos": [
    {
      "id": 45,
      "codigo": "PROD045",
      "abc": "A",
      "saldo_manut": 0,
      "cmm": 25.5,
      "tipo": 10
    },
    {
      "id": 78,
      "codigo": "PROD078",
      "abc": "A",
      "saldo_manut": 0,
      "cmm": 18.2,
      "tipo": 19
    }
  ]
}
```

---

#### **Estatísticas Gerais**
```http
GET /api/produtos/estatisticas
```

Retorna estatísticas agregadas do estoque.

**Response (200 OK):**
```json
{
  "success": true,
  "estatisticas": {
    "total_produtos": 1250,
    "produtos_ativos": 1180,
    "produtos_inativos": 70,
    "total_por_abc": {
      "A": 450,
      "B": 380,
      "C": 350
    },
    "total_por_tipo": {
      "10": 600,
      "19": 400,
      "20": 180
    },
    "valor_total_estoque": 2500000.50,
    "cmm_medio": 12.5,
    "produtos_criticos": 25
  }
}
```

---

## 🧪 Interface de Testes

### 🎨 test_login.html

Interface web moderna para testar os endpoints de autenticação.

**Funcionalidades:**

- ✅ Status da API em tempo real
- ✅ Formulário de Login
- ✅ Formulário de Cadastro com níveis dinâmicos
- ✅ Console visual de logs
- ✅ Verificações automáticas de segurança
- ✅ Design responsivo e moderno

### 🚀 Como Usar

1. **Inicie o servidor**:
```bash
python app.py
```

2. **Abra a interface**:
```bash
.\abrir_teste.bat
```
ou abra `test_login.html` diretamente no navegador

3. **Cadastre um usuário**:
   - Email: teste@nexum.com
   - Senha: Teste@123
   - Matrícula: MAT001
   - Nível: (será carregado dinamicamente)

4. **Faça login** com as mesmas credenciais

### 🔍 Verificações Automáticas

O sistema realiza verificações em **3 camadas**:

#### 1. Frontend (JavaScript)

```javascript
// Verifica estrutura do objeto User
const expectedFields = ['id', 'email', 'matricula', 'nivel_acesso', 'data_criacao', 'data_atualizacao'];
const missingFields = expectedFields.filter(field => !(field in data.user));

// Alerta se senha estiver na resposta
if ('senha' in data.user) {
    console.error('🔴 ALERTA DE SEGURANÇA: Senha está sendo retornada!');
}
```

#### 2. Backend (Python - Logs)

```python
# Em user_service.py
print(f"✅ Tipo do objeto: {type(user)}")
print(f"✅ É instância de User? {user.__class__.__name__ == 'User'}")
print(f"✅ Campos no dict: {list(user_dict.keys())}")
print(f"✅ Senha incluída? {'senha' in user_dict}")
```

#### 3. Console Visual

- Timestamp de cada operação
- Status HTTP com cores (verde/vermelho)
- Request e Response formatados em JSON
- Senhas mascaradas nos logs

### 📊 Exemplo de Logs

**No Terminal (Python):**
```
================================================================================
🔍 LOGIN - VERIFICAÇÃO DE INSTÂNCIA
================================================================================
✅ Tipo do objeto: <class 'models.user.User'>
✅ É instância de User? True
✅ Representação: <User(id=1, email=teste@nexum.com, matricula=MAT001, nivel=planejador)>
✅ Atributos: id=1, email=teste@nexum.com, matricula=MAT001
================================================================================

✅ Conversão User -> Dict realizada com sucesso
✅ Campos no dict: ['id', 'email', 'matricula', 'nivel_acesso', 'data_criacao', 'data_atualizacao']
✅ Senha incluída? False
```

**No Console do Navegador (F12):**
```
🔍 Verificação do objeto User recebido:
{
  id: 1,
  email: "teste@nexum.com",
  matricula: "MAT001",
  nivel_acesso: "planejador",
  data_criacao: "2025-10-15 10:30:00",
  data_atualizacao: "2025-10-15 10:30:00"
}

✅ Campos do User: ['id', 'email', 'matricula', 'nivel_acesso', 'data_criacao', 'data_atualizacao']
✅ Todos os campos esperados estão presentes!
✅ Segurança OK: Senha não foi retornada na resposta
```

---

## 🏛️ Arquitetura

### 📐 Padrões de Design

O projeto segue boas práticas de arquitetura de software:

#### **MVC + Repository Pattern**

```
┌─────────────────────────────────────┐
│         PRESENTATION LAYER          │
│    (Controllers - API Routes)       │
│  • Recebe HTTP requests             │
│  • Retorna HTTP responses           │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│         BUSINESS LAYER              │
│      (Services - Logic)             │
│  • Validações de negócio            │
│  • Transformações de dados          │
│  • Regras de autenticação           │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│         DATA ACCESS LAYER           │
│    (Repositories - SQL)             │
│  • Queries ao banco                 │
│  • Conversão de dados               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│         DATA LAYER                  │
│     (Models - Entities)             │
│  • Representação de dados           │
│  • Métodos auxiliares               │
└─────────────────────────────────────┘
```

### 🔄 Fluxo de Dados Completo

**Exemplo: Login de Usuário**

```
1. Cliente (test_login.html)
   │
   ├─► POST /api/users/login
   │   { "email": "user@test.com", "senha": "Pass@123" }
   │
2. Controller (user_controller.py)
   │
   ├─► Valida JSON recebido
   ├─► Extrai email e senha
   │
   └─► Chama: user_service.login(email, senha)
       │
3. Service (user_service.py)
       │
       ├─► Valida entrada
       │
       └─► Chama: user_repository.find_by_email(email)
           │
4. Repository (user_repository.py)
           │
           ├─► Executa: SELECT * FROM usuarios WHERE email = ?
           │
           └─► Retorna: User object
               │
5. Service (user_service.py)
               │
               ├─► Verifica senha com bcrypt.checkpw()
               │
               └─► Se válido: user.to_dict(include_senha=False)
                   │
6. Controller (user_controller.py)
                   │
                   └─► jsonify({ "success": true, "user": {...} })
                       │
7. Cliente (test_login.html)
                       │
                       └─► Exibe dados do usuário
```

### 🔌 Separação de Responsabilidades

| Camada | Responsabilidade | Não deve fazer |
|--------|------------------|----------------|
| **Model** | Representar dados | Lógica de negócio, SQL |
| **Repository** | Acesso ao banco | Validações, transformações |
| **Service** | Lógica de negócio | SQL direto, HTTP |
| **Controller** | Rotas HTTP | Lógica complexa, SQL |

---

## 🐛 Troubleshooting

### ❌ Erro: "pyodbc.InterfaceError: Data source name not found"

**Causa**: Driver ODBC não instalado ou nome incorreto

**Solução**:
1. Instale o driver: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
2. Verifique o nome exato:
```powershell
# Windows PowerShell
Get-OdbcDriver | Where-Object {$_.Name -like "*SQL Server*"}
```
3. Atualize o `.env` com o nome correto

---

### ❌ Erro: "Login failed for user"

**Causa**: Credenciais incorretas ou firewall bloqueando

**Solução**:
1. Verifique usuário e senha no Portal Azure
2. Adicione seu IP ao firewall (ver seção Configurar Firewall)
3. Teste com Azure Data Studio primeiro

---

### ❌ Erro: "Module not found: bcrypt"

**Causa**: Dependências não instaladas

**Solução**:
```bash
pip install -r requirements.txt
```

---

### ❌ API retorna "CORS error"

**Causa**: CORS não configurado adequadamente

**Solução**: O CORS já está habilitado em `app.py`, mas verifique se o servidor está rodando:
```python
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": "*"
    }
})
```

---

### ❌ Erro: "Senha deve conter pelo menos um caractere especial"

**Causa**: Senha não atende aos requisitos

**Solução**: Use senha com:
- Mínimo 8 caracteres
- 1 maiúscula (A-Z)
- 1 minúscula (a-z)
- 1 número (0-9)
- 1 especial (!@#$%...)

**Exemplo válido**: `Teste@123`

---

### ❌ Níveis de acesso não aparecem no select

**Causa**: API offline ou erro no endpoint `/api/users/niveis-acesso`

**Solução**:
1. Verifique se o servidor está rodando
2. Abra DevTools (F12) → Network
3. Veja se a requisição GET /api/users/niveis-acesso foi feita
4. Em caso de erro, o sistema usa valores padrão

---

### 🔍 Debug de Conexão

Use o script de teste:
```bash
python aux_files/test_connection.py
```

Se falhar, verifique:
1. ✅ Arquivo `.env` existe e está preenchido
2. ✅ Driver ODBC instalado
3. ✅ Firewall do Azure configurado
4. ✅ Credenciais corretas

---

## 📚 Recursos Adicionais

### 📖 Documentação

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/)
- [bcrypt Documentation](https://github.com/pyca/bcrypt/)
- [PyODBC Documentation](https://github.com/mkleehammer/pyodbc/wiki)

### 🛠️ Ferramentas Recomendadas

- **Azure Data Studio**: GUI para SQL Server
- **Postman**: Testar APIs
- **VS Code**: Editor de código com extensões Python
- **Git**: Controle de versão

### 📝 Scripts Úteis

```bash
# Gerar hash de senha
python gerar_hash.py

# Testar conexão com banco
python aux_files/test_connection.py

# Rodar testes automatizados
python test_api.py

# Debug de login específico
python debug_login.py
```

---

## 👥 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autores

- **BBTS-Nexum Team**
- GitHub: [@BBTS-Nexum](https://github.com/BBTS-Nexum)

---

## 🙏 Agradecimentos

- Stefanini Group
- Microsoft Azure
- Comunidade Python Brasil

---

<div align="center">

**Feito com ❤️ pela equipe Nexum**

[⬆ Voltar ao topo](#-nexum-supply-chain---backend-api)

</div>
