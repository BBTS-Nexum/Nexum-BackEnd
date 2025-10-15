# 🚀 Nexum Supply Chain API# 📦 Nexum Supply Chain - Backend API# 📦 Nexum Supply Chain - Backend API



> **API REST para gestão inteligente de estoque com classificação ABC, tipologia de materiais e cálculos automatizados de planejamento de compras**



Sistema desenvolvido para o **Hackathon Stefanini 2025** - Solução para substituir planilhas manuais por um sistema escalável, transparente e com suporte à decisão baseada em dados.> Sistema completo de gerenciamento de cadeia de suprimentos com autenticação segura, rastreabilidade em tempo real e API REST robusta.> Sistema completo de gerenciamento de cadeia de suprimentos com autenticação segura, rastreabilidade em tempo real e API REST robusta.



---



## 📑 Índice[![Azure](https://img.shields.io/badge/Azure-SQL_Database-0078D4?logo=microsoftazure)](https://azure.microsoft.com)[![Azure](https://img.shields.io/badge/Azure-SQL_Database-0078D4?logo=microsoftazure)](https://azure.microsoft.com)



- [Visão Geral](#-visão-geral)[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)](https://www.python.org)[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)](https://www.python.org)

- [Tecnologias](#-tecnologias)

- [Configuração do Ambiente](#-configuração-do-ambiente)[![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?logo=flask)](https://flask.palletsprojects.com)[![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?logo=flask)](https://flask.palletsprojects.com)

- [Arquitetura](#-arquitetura)

- [Campos do Banco de Dados](#-campos-do-banco-de-dados)[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

- [Cálculos e Regras de Negócio](#-cálculos-e-regras-de-negócio)

- [Endpoints da API](#-endpoints-da-api)

- [Exemplos de Uso](#-exemplos-de-uso)

- [Documentação Swagger](#-documentação-swagger)------



---



## 🎯 Visão Geral## 📑 Índice## 📑 Índice



### O Problema



Operação com mais de **5.000 SKUs** em **32 CDAs** espalhados pelo Brasil, onde o planejamento de aquisições é feito manualmente em Excel:- [Visão Geral](#-visão-geral)- [Visão Geral](#-visão-geral)



- ❌ Dados dispersos (ERP, SharePoint, e-mails)- [Quick Start](#-quick-start)- [Quick Start](#-quick-start)

- ❌ Falta de rastreabilidade

- ❌ Decisões lentas baseadas em dados desatualizados- [Estrutura do Projeto](#-estrutura-do-projeto)- [Estrutura do Projeto](#-estrutura-do-projeto)

- ❌ Rupturas de estoque e excessos

- [Configuração do Ambiente](#️-configuração-do-ambiente)- [Configuração do Ambiente](#-configuração-do-ambiente)

### A Solução

- [Banco de Dados](#️-banco-de-dados)- [Banco de Dados](#-banco-de-dados)

Sistema que oferece:

- [Sistema de Autenticação](#-sistema-de-autenticação)- [Sistema de Autenticação](#-sistema-de-autenticação)

- ✅ **Visualização em tempo real** via API REST

- ✅ **Centralização** em banco Azure SQL- [API Endpoints](#-api-endpoints)- [API Endpoints](#-api-endpoints)

- ✅ **Alertas inteligentes** (produtos críticos, cobertura baixa)

- ✅ **Cálculos automatizados** (ES, FA, QA)- [Interface de Testes](#-interface-de-testes)- [Testes](#-testes)

- ✅ **Sugestões de compra** baseadas em histórico

- ✅ **Previsibilidade** com indicadores de cobertura- [Arquitetura](#️-arquitetura)- [Arquitetura](#-arquitetura)



---- [Troubleshooting](#-troubleshooting)- [Deployment](#-deployment)



## 🛠 Tecnologias- [Troubleshooting](#-troubleshooting)



- **Python 3.13.7** - Linguagem principal---

- **Flask 3.1.2** - Framework web

- **Azure SQL Database** - Banco de dados em nuvem

- **pyodbc 5.2.0** - Conector SQL Server## 🎯 Visão Geral

- **bcrypt 4.1.2** - Hash de senhas

- **flask-cors 6.0.1** - CORS

- **flask-swagger-ui 5.21.0** - Documentação interativaO **Nexum Supply Chain Backend** é uma API REST construída com Flask que oferece:



---O **Nexum Supply Chain Backend** é uma API REST construída com Flask que oferece:



## ⚙️ Configuração do Ambiente- 🔐 **Autenticação Segura**: Sistema completo de login com bcrypt e validações robustas



### 1. Clonar o Repositório- 📊 **Gestão de Usuários**: CRUD completo com diferentes níveis de acesso- 🔐 **Autenticação Segura**: Sistema completo de login com bcrypt e validações robustas



```bash- 🔄 **Níveis Dinâmicos**: Carregamento automático de níveis de acesso do banco- 📊 **Gestão de Usuários**: CRUD completo com diferentes níveis de acesso

git clone https://github.com/BBTS-Nexum/Nexum-BackEnd.git

cd Nexum-BackEnd- 🛡️ **Segurança**: Senhas hasheadas, validações de email e senha forte- 🔄 **Níveis Dinâmicos**: Carregamento automático de níveis de acesso do banco

```

- 📈 **Rastreabilidade**: Logs detalhados de todas as operações- 🛡️ **Segurança**: Senhas hasheadas, validações de email e senha forte

### 2. Criar Ambiente Virtual

- 🎨 **Interface de Testes**: HTML/JS para testar endpoints facilmente- 📈 **Rastreabilidade**: Logs detalhados de todas as operações

```powershell

python -m venv NexumEnv- 🎨 **Interface de Testes**: HTML/JS para testar endpoints facilmente

.\NexumEnv\Scripts\Activate.ps1

```### ✨ Funcionalidades Principais



### 3. Instalar Dependências- ✅ Login e cadastro de usuários



```bash- ✅ Alteração de senha com validação- ✅ Login e cadastro de usuários

pip install -r requirements.txt

```- ✅ Busca de usuários por email, matrícula ou ID- ✅ Alteração de senha com validação



### 4. Configurar Variáveis de Ambiente- ✅ Listagem de todos os usuários- ✅ Busca de usuários por email, matrícula ou ID



Crie um arquivo `.env` na raiz:- ✅ Níveis de acesso dinâmicos (planejador, comprador, fiscal, gestor)- ✅ Listagem de todos os usuários



```env- ✅ CORS habilitado para integração com frontend- ✅ Níveis de acesso dinâmicos (planejador, comprador, fiscal, gestor)

DB_SERVER=seu-servidor.database.windows.net

DB_DATABASE=stefanini_app- ✅ Validações robustas de entrada- ✅ CORS habilitado para integração com frontend

DB_USERNAME=seu-usuario

DB_PASSWORD=sua-senha- ✅ Tratamento de erros adequado- ✅ Validações robustas de entrada

DB_DRIVER=ODBC Driver 18 for SQL Server

```- ✅ Tratamento de erros adequado



### 5. Executar o Servidor---



```bash## 🚀 Quick Start

python app.py

```### **1. Clone o Repositório**



Servidor disponível em: **http://localhost:5000**  ```bash### **1. Clone o Repositório**

Documentação Swagger: **http://localhost:5000/docs**

git clone https://github.com/BBTS-Nexum/Nexum-BackEnd.git```bash

---

cd Nexum-BackEndgit clone https://github.com/BBTS-Nexum/Nexum-BackEnd.git

## 🏗 Arquitetura

```cd Nexum-BackEnd

```

Nexum-BackEnd/```

├── app.py                      # Aplicação principal Flask

├── controllers/                # Camada de rotas (endpoints)### **2. Crie o Ambiente Virtual**

│   ├── user_controller.py

│   └── produto_controller.py```bash### **2. Crie o Ambiente Virtual**

├── services/                   # Camada de lógica de negócio

│   ├── user_service.py# Windows PowerShell```bash

│   └── produto_service.py

├── repositories/               # Camada de acesso a dadospython -m venv NexumEnv# Windows PowerShell

│   ├── user_repository.py

│   └── produto_repository.py.\NexumEnv\Scripts\Activate.ps1python -m venv NexumEnv

├── models/                     # Modelos de dados

│   ├── user.py.\NexumEnv\Scripts\Activate.ps1

│   └── produto.py

├── database/                   # Scripts SQL# Linux/Mac

│   └── create_table.sql

├── swagger.json                # Especificação OpenAPIpython3 -m venv NexumEnv# Linux/Mac

└── requirements.txt            # Dependências Python

```source NexumEnv/bin/activatepython3 -m venv NexumEnv



**Padrão de Arquitetura**: MVC com Repository Pattern```source NexumEnv/bin/activate



---```



## 📊 Campos do Banco de Dados### **3. Instale as Dependências**



### Tabela: `supply_chain.produtos_estoque````bash### **3. Instale as Dependências**



#### **Identificação**pip install -r requirements.txt```bash

- `id` (INT) - Chave primária auto-incremento

- `codigo` (NVARCHAR(50)) - Código único do produto```pip install -r requirements.txt



#### **Classificação**```

- `abc` (CHAR(1)) - Classificação ABC: **'A'** (alta prioridade), **'B'** (média), **'C'** (baixa)

- `tipo` (INT) - Tipologia: **10** (reparável), **19** (testável), **20** (descartável)### **4. Configure o Banco de Dados**



#### **Peças Boas** (Disponíveis para Uso)### **4. Configure o Banco de Dados**

- `saldo_manut` (INT) - Peças disponíveis no Manut para o CAT

- `provid_compras` (INT) - Peças que irão chegar (compradas)Crie o arquivo `.env` com suas credenciais do Azure:

- `recebimento_esperado` (INT) - Peças recebidas mas ainda não no estoque

- `transito_manut` (INT) - Peças em trânsito entre unidadesCrie o arquivo `.env` com suas credenciais do Azure:

- `stage_manut` (INT) - Peças reservadas

- `recepcao_manut` (INT) - Peças em recebimento```bash

- `pendente_ri` (INT) - Peças entre recepção e recebimento

# Copie o exemplo```bash

#### **Peças em Teste**

- `pecas_teste` (INT) - Com técnicos de atendimentoCopy-Item .env.example .env# Copie o exemplo

- `pecas_teste_kit` (INT) - Atendimentos distantes de um CAT

Copy-Item .env.example .env

#### **Peças para Reparo** (Defeituosas)

- `fornecedor_reparo` (INT) - Com reparador externo# Edite com suas credenciais

- `laboratorio` (INT) - Em centros de reparo BBTS

- `wr` (INT) - Aguardando envio para reparonotepad .env# Edite com suas credenciais

- `wrcr` (INT) - Atendidas em CR, aguardando reparador externo

- `stage_wr` (INT) - Reservadas para reparo```notepad .env



#### **Métricas e KPIs**```

- `cmm` (DECIMAL(10,2)) - Consumo Médio Mensal

- `coef_perda` (DECIMAL(10,8)) - Percentual histórico de peças irreparáveisPreencha o `.env`:



#### **Auditoria**```envPreencha o `.env`:

- `data_criacao` (DATETIME2) - Data de criação do registro

- `data_atualizacao` (DATETIME2) - Última atualizaçãoAZURE_SQL_DRIVER=ODBC Driver 18 for SQL Server```env

- `usuario_criacao` (NVARCHAR(100)) - Quem criou

- `usuario_atualizacao` (NVARCHAR(100)) - Quem atualizouAZURE_SQL_SERVER=seu-servidor.database.windows.netAZURE_SQL_DRIVER=ODBC Driver 18 for SQL Server

- `ativo` (BIT) - Registro ativo/inativo

AZURE_SQL_PORT=1433AZURE_SQL_SERVER=seu-servidor.database.windows.net

---

AZURE_SQL_DATABASE=stefanini_appAZURE_SQL_PORT=1433

## 🧮 Cálculos e Regras de Negócio

AZURE_SQL_USERNAME=seu-usuarioAZURE_SQL_DATABASE=seu-database

### 1️⃣ **Peças Boas (Total)**

```AZURE_SQL_PASSWORD=sua-senhaAZURE_SQL_USERNAME=seu-usuario

Peças_Boas = saldo_manut + provid_compras + recebimento_esperado + 

             transito_manut + stage_manut + recepcao_manut + pendente_riAZURE_SQL_ENCRYPT=yesAZURE_SQL_PASSWORD=sua-senha

```

AZURE_SQL_TRUST_SERVER_CERTIFICATE=noAZURE_SQL_ENCRYPT=yes

### 2️⃣ **Peças em Teste (Total)**

```AZURE_SQL_CONNECTION_TIMEOUT=30AZURE_SQL_TRUST_SERVER_CERTIFICATE=no

Peças_Teste = pecas_teste + pecas_teste_kit

``````AZURE_SQL_CONNECTION_TIMEOUT=30



### 3️⃣ **Peças para Reparo (Total)**```

```

Peças_Reparo = fornecedor_reparo + laboratorio + wr + wrcr + stage_wr### **5. Execute os Scripts SQL**

```

### **5. Execute os Scripts SQL**

### 4️⃣ **Saldo Total (por Tipo)**

No Azure Data Studio, execute na ordem:

**Para T-10 e T-19 (Reparáveis/Testáveis):**

```1. `database/create_users_table.sql` - Cria tabela de usuáriosNo Azure Data Studio, execute na ordem:

Saldo_Total = Peças_Boas + Peças_Teste + Peças_Reparo - (Peças_Reparo × coef_perda)

```2. `database/create_table.sql` - Cria tabela de produtos (opcional)1. `database/create_users_table.sql` - Cria tabela de usuários



**Para T-20 (Descartáveis):**2. `database/create_table.sql` - Cria tabela de produtos (opcional)

```

Saldo_Total = Peças_Boas### **6. Inicie o Servidor**

```

```bash### **6. Inicie o Servidor**

### 5️⃣ **Estoque de Segurança (ES)**

python app.py```bash

| ABC | Tipo | Fórmula |

|-----|------|---------|```python app.py

| A | T-10 ou T-19 | `ES = 4 × CMM` |

| A | T-20 | `ES = 1.5 × CMM` |```

| B ou C | T-10 ou T-19 | `ES = 5 × CMM` |

| B ou C | T-20 | `ES = 2.5 × CMM` |✅ Servidor rodando em: **http://localhost:5000**



### 6️⃣ **Fator de Ajuste (FA)**✅ Servidor rodando em: http://localhost:5000



**Para T-10 e T-19:**### **7. Teste a API**

```

FA = ES + (4 × CMM × coef_perda)Abra o arquivo de testes no navegador:

```

```bashAbra o arquivo de testes no navegador:

**Para T-20:**

```# Abre interface de testes```bash

FA = ES + (4 × CMM)

```.\abrir_teste.bat# Abre interface de testes



*O `4 × CMM` representa a cobertura de leadtime (~4 meses)*.\abrir_teste.bat



### 7️⃣ **Quantidade a Adquirir (QA)**# Ou abra manualmente

```

QA = max(0, FA - Saldo_Total)start test_login.html# Ou abra manualmente

```

```start test_login.html

- **QA > 0**: Precisa comprar

- **QA = 0**: Estoque suficiente```



### 8️⃣ **Cobertura em Meses**---

```

Cobertura = Saldo_Total / CMM## 📁 Estrutura do Projeto

```



### 9️⃣ **Status do Estoque**```



| Status | Condição |Nexum-BackEnd/```

|--------|----------|

| **critico** | QA > 0 (precisa comprar) |│Nexum-BackEnd/

| **baixo** | Cobertura < 2 meses |

| **ok** | Cobertura ≥ 2 meses |├── app.py                      # 🚀 Aplicação Flask principal│



---├── requirements.txt            # 📦 Dependências Python├── app.py                      # Aplicação Flask principal



## 🌐 Endpoints da API├── .env                        # 🔐 Configurações (não commitado)├── requirements.txt            # Dependências Python



### **Autenticação**├── .env.example               # 📄 Exemplo de configurações├── .env                        # Configurações (não commitado)



#### `POST /api/usuarios/login`│├── .env.example               # Exemplo de configurações

Login de usuário

├── models/                    # 🎯 Modelos de dados│

**Body:**

```json│   └── user.py               #    └─ Classe User├── models/                    # Modelos de dados

{

  "email": "admin@nexum.com",││   └── user.py               # Classe User

  "senha": "senha123"

}├── repositories/             # 🗄️ Camada de acesso a dados│

```

│   └── user_repository.py   #    └─ Queries SQL para usuários├── repositories/             # Camada de acesso a dados

**Response 200:**

```json││   └── user_repository.py   # Queries SQL para usuários

{

  "id": 1,├── services/                # ⚙️ Lógica de negócio│

  "nome": "Admin",

  "email": "admin@nexum.com",│   └── user_service.py     #    └─ Validações e bcrypt├── services/                # Lógica de negócio

  "nivel_acesso": 1

}││   └── user_service.py     # Validações e bcrypt

```

├── controllers/            # 🎮 Rotas da API│

#### `POST /api/usuarios/registrar`

Registrar novo usuário│   └── user_controller.py #    └─ Endpoints REST├── controllers/            # Rotas da API



**Body:**││   └── user_controller.py # Endpoints REST

```json

{├── database/              # 💾 Scripts SQL│

  "nome": "João Silva",

  "email": "joao@nexum.com",│   ├── create_users_table.sql├── database/              # Scripts SQL

  "senha": "senha123",

  "nivel_acesso": 2│   ├── create_table.sql│   ├── create_users_table.sql

}

```│   └── README.md│   ├── create_table.sql



---││   └── README.md



### **Usuários**├── aux_files/            # 🛠️ Utilitários│



#### `GET /api/usuarios/`│   ├── sql.py           #    ├─ Helper de conexão├── aux_files/            # Utilitários

Listar todos os usuários

│   ├── test_connection.py  # └─ Teste de conexão│   ├── sql.py           # Helper de conexão

#### `GET /api/usuarios/niveis-acesso`

Retorna mapeamento de níveis de acesso│   └── analise_dados.py    #    └─ Análise de dados│   ├── test_connection.py



---││   └── analise_dados.py



### **Produtos - CRUD**├── test_login.html      # 🧪 Interface de testes│



#### `GET /api/produtos/`├── test_login.js        # 📝 Lógica de testes├── test_login.html      # Interface de testes

Listar produtos com paginação

├── test_api.py         # 🤖 Testes automatizados├── test_login.js        # Lógica de testes

**Query Params:**

- `page` (default: 1)├── debug_login.py      # 🐛 Debug de login├── test_api.py         # Testes automatizados

- `per_page` (default: 50)

├── gerar_hash.py       # 🔒 Utilitário para gerar hash├── debug_login.py      # Debug de login

#### `POST /api/produtos/`

Criar novo produto├── abrir_teste.bat     # ⚡ Script para abrir testes├── gerar_hash.py       # Utilitário para gerar hash



**Body:**││

```json

{└── NexumEnv/          # 🐍 Ambiente virtual (não commitado)└── NexumEnv/          # Ambiente virtual (não commitado)

  "codigo": "MAT-001",

  "abc": "A",``````

  "tipo": 10,

  "saldo_manut": 100,

  "cmm": 25.5,

  "coef_perda": 0.05------

}

```



#### `GET /api/produtos/{id}`## ⚙️ Configuração do Ambiente## ⚙️ Configuração do Ambiente

Buscar produto por ID



#### `GET /api/produtos/codigo/{codigo}`

Buscar produto por código### 📋 Variáveis de Ambiente (.env)### Variáveis de Ambiente (.env)



#### `PUT /api/produtos/{id}`

Atualizar produto

O sistema usa um arquivo `.env` para configurações sensíveis:O sistema usa um arquivo `.env` para configurações sensíveis:

#### `DELETE /api/produtos/{id}`

Deletar produto (soft delete)



---```env```env



### **Produtos - Consultas**# Azure SQL Database# Azure SQL Database



#### `GET /api/produtos/criticos`AZURE_SQL_DRIVER=ODBC Driver 18 for SQL ServerAZURE_SQL_DRIVER=ODBC Driver 18 for SQL Server

Produtos com estoque crítico

AZURE_SQL_SERVER=nexum-server.database.windows.netAZURE_SQL_SERVER=nexum-server.database.windows.net

**Query Params:**

- `limit` (default: 100, max: 1000)AZURE_SQL_PORT=1433AZURE_SQL_PORT=1433



#### `GET /api/produtos/estatisticas`AZURE_SQL_DATABASE=stefanini_appAZURE_SQL_DATABASE=stefanini_app

Estatísticas gerais do estoque

AZURE_SQL_USERNAME=nexumadminAZURE_SQL_USERNAME=nexumadmin

**Response:**

```jsonAZURE_SQL_PASSWORD=SuaSenhaSegura123!AZURE_SQL_PASSWORD=SuaSenhaSegura123!

{

  "success": true,AZURE_SQL_ENCRYPT=yesAZURE_SQL_ENCRYPT=yes

  "estatisticas": {

    "total_produtos": 1250,AZURE_SQL_TRUST_SERVER_CERTIFICATE=noAZURE_SQL_TRUST_SERVER_CERTIFICATE=no

    "produtos_criticos": 45,

    "por_abc": {AZURE_SQL_CONNECTION_TIMEOUT=30AZURE_SQL_CONNECTION_TIMEOUT=30

      "A": 300,

      "B": 450,``````

      "C": 500

    },

    "por_tipo": {

      "reparavel": 600,### 🔑 Obter Credenciais do Azure### Obter Credenciais do Azure

      "testavel": 400,

      "descartavel": 250

    }

  }1. Acesse https://portal.azure.com1. Acesse https://portal.azure.com

}

```2. Navegue até seu **SQL Database**2. Navegue até seu SQL Database



---3. Clique em **"Connection strings"**3. Clique em **"Connection strings"**



### **Indicadores e Planejamento**4. Copie a string **ODBC**4. Copie a string **ODBC**



#### `GET /api/produtos/{id}/indicadores`5. Extraia os valores para o `.env`5. Extraia os valores para o `.env`

Retorna todos os indicadores calculados para um produto



**Response 200:**

```json**Exemplo de connection string do Azure:**### Configurar Firewall do Azure

{

  "success": true,```

  "produto": {

    "id": 1,Driver={ODBC Driver 18 for SQL Server};⚠️ **IMPORTANTE**: Adicione seu IP ao firewall!

    "codigo": "MAT-001",

    "abc": "A",Server=tcp:nexum-server.database.windows.net,1433;

    "tipo": 10,

    "tipo_nome": "reparavel",Database=stefanini_app;1. No Azure Portal, vá ao **SQL Server** (não Database)

    "saldo_manut": 100,

    "cmm": 25.5,Uid=nexumadmin;2. Menu lateral → **"Networking"**

    "coef_perda": 0.05,

    "saldo_total": 185.5,Pwd={your_password_here};3. Clique **"Add client IP"**

    "indicadores": {

      "pecas_boas": 150,Encrypt=yes;4. Ative **"Allow Azure services..."**

      "pecas_teste": 20,

      "pecas_reparo": 30,```5. Clique **"Save"**

      "estoque_seguranca": 102,

      "fator_ajuste": 107.1,

      "quantidade_adquirir": 0,

      "cobertura_meses": 7.27,**Como preencher o .env:**### Dependências Principais

      "status": "ok"

    }- `AZURE_SQL_SERVER`: nexum-server.database.windows.net (sem `tcp:` e sem `,1433`)

  }

}- `AZURE_SQL_DATABASE`: stefanini_app```

```

- `AZURE_SQL_USERNAME`: nexumadminFlask==3.1.2           # Framework web

#### `GET /api/produtos/necessidade-compra`

Lista produtos que precisam ser comprados (QA > 0)- `AZURE_SQL_PASSWORD`: Sua senha realflask-cors==6.0.1      # CORS support



**Query Params:**bcrypt==4.1.2          # Hash de senhas

- `limit` (default: 100, max: 1000)

### 🔥 Configurar Firewall do Azurepyodbc==5.2.0          # Conexão SQL Server

**Response:**

```jsonpython-dotenv==1.0.1   # Variáveis de ambiente

{

  "success": true,⚠️ **MUITO IMPORTANTE**: O Azure bloqueia todas as conexões por padrão!flasgger==0.9.7.1      # Documentação Swagger (futuro)

  "total": 15,

  "produtos": [```

    {

      "codigo": "MAT-005",1. No Azure Portal, vá ao **SQL Server** (não o Database)

      "abc": "A",

      "tipo_nome": "descartavel",2. Menu lateral → **"Networking"** ou **"Firewalls and virtual networks"**---

      "saldo_total": 20,

      "indicadores": {3. Clique **"Add client IP"** (adiciona seu IP automaticamente)

        "quantidade_adquirir": 45.5,

        "cobertura_meses": 0.8,4. Ative **"Allow Azure services and resources to access this server"**## 🗄️ Banco de Dados

        "status": "critico"

      }5. Clique **"Save"**

    }

  ]### Tabela: `supply_chain.usuarios`

}

```### 📦 Dependências Principais



#### `GET /api/produtos/cobertura-baixa````sql

Lista produtos com cobertura menor que X meses

```txtCREATE TABLE supply_chain.usuarios (

**Query Params:**

- `meses` (default: 2)Flask==3.1.2           # Framework web    id INT IDENTITY(1,1) PRIMARY KEY,

- `limit` (default: 100, max: 1000)

flask-cors==6.0.1      # CORS support    email NVARCHAR(255) NOT NULL UNIQUE,

---

bcrypt==4.1.2          # Hash de senhas    senha VARCHAR(255) NOT NULL,          -- Hash bcrypt

### **Tipologia**

pyodbc==5.2.0          # Conexão SQL Server    matricula NVARCHAR(50) NOT NULL UNIQUE,

#### `GET /api/produtos/tipos`

Retorna tipos de materiais disponíveispython-dotenv==1.0.1   # Variáveis de ambiente    nivel_acesso NVARCHAR(50) NOT NULL,   



**Response:**pytest==8.4.0          # Testes    data_criacao DATETIME2 NOT NULL DEFAULT GETDATE(),

```json

{coverage==7.11.0       # Cobertura de testes    data_atualizacao DATETIME2 NOT NULL DEFAULT GETDATE(),

  "success": true,

  "tipos": [```    

    {

      "codigo": 10,    CONSTRAINT CK_usuarios_nivel_acesso 

      "nome": "reparavel",

      "descricao": "Peças 100% reparáveis",---        CHECK (nivel_acesso IN ('planejador', 'comprador', 'fiscal', 'gestor')),

      "emoji": "♻️",

      "calculo_saldo": "saldo + teste + reparo - perdas"    CONSTRAINT CK_usuarios_email_valido 

    },

    {## 🗄️ Banco de Dados        CHECK (email LIKE '%_@__%.__%')

      "codigo": 19,

      "nome": "testavel",)

      "descricao": "Peças passíveis de teste",

      "emoji": "🔍",### 📊 Tabela: `supply_chain.usuarios````

      "calculo_saldo": "saldo + teste + reparo - perdas"

    },

    {

      "codigo": 20,```sql### Níveis de Acesso

      "nome": "descartavel",

      "descricao": "Peças de uso único",CREATE TABLE supply_chain.usuarios (

      "emoji": "🗑️",

      "calculo_saldo": "apenas saldo"    id INT IDENTITY(1,1) PRIMARY KEY,- **planejador**: Planejador de Supply Chain

    }

  ]    email NVARCHAR(255) NOT NULL UNIQUE,- **comprador**: Responsável por compras

}

```    senha VARCHAR(255) NOT NULL,          -- Hash bcrypt- **fiscal**: Fiscal de contratos



---    matricula NVARCHAR(50) NOT NULL UNIQUE,- **gestor**: Gestor/Administrador



## 💡 Exemplos de Uso    nivel_acesso NVARCHAR(50) NOT NULL,   



### Python    data_criacao DATETIME2 NOT NULL DEFAULT GETDATE(),### Índices



```python    data_atualizacao DATETIME2 NOT NULL DEFAULT GETDATE(),

import requests

    ```sql

# Login

response = requests.post('http://localhost:5000/api/usuarios/login', json={    CONSTRAINT CK_usuarios_nivel_acesso -- Performance em login

    'email': 'admin@nexum.com',

    'senha': 'senha123'        CHECK (nivel_acesso IN ('planejador', 'comprador', 'fiscal', 'gestor')),CREATE NONCLUSTERED INDEX IX_usuarios_email 

})

user = response.json()    CONSTRAINT CK_usuarios_email_valido     ON supply_chain.usuarios(email)



# Listar produtos        CHECK (email LIKE '%_@__%.__%')

response = requests.get('http://localhost:5000/api/produtos/', params={

    'page': 1,)-- Performance em busca por matrícula  

    'per_page': 10

})```CREATE NONCLUSTERED INDEX IX_usuarios_matricula 

produtos = response.json()

    ON supply_chain.usuarios(matricula)

# Ver indicadores de um produto

response = requests.get('http://localhost:5000/api/produtos/1/indicadores')### 👥 Níveis de Acesso

indicadores = response.json()

print(f"QA: {indicadores['produto']['indicadores']['quantidade_adquirir']}")-- Performance em filtro por nível



# Listar produtos que precisam de compra| Nível | Descrição | Permissões |CREATE NONCLUSTERED INDEX IX_usuarios_nivel_acesso 

response = requests.get('http://localhost:5000/api/produtos/necessidade-compra')

para_comprar = response.json()|-------|-----------|------------|    ON supply_chain.usuarios(nivel_acesso)

print(f"Total a comprar: {para_comprar['total']}")

```| **planejador** | Planejador de Supply Chain | Visualização e análise de dados |```



### cURL| **comprador** | Responsável por compras | Gestão de pedidos e fornecedores |



```bash| **fiscal** | Fiscal de contratos | Auditoria e conformidade |---

# Login

curl -X POST http://localhost:5000/api/usuarios/login \| **gestor** | Gestor/Administrador | Acesso total ao sistema |

  -H "Content-Type: application/json" \

  -d '{"email":"admin@nexum.com","senha":"senha123"}'## 🔐 Sistema de Autenticação



# Criar produto### 📈 Índices para Performance

curl -X POST http://localhost:5000/api/produtos/ \

  -H "Content-Type: application/json" \---

  -d '{

    "codigo": "MAT-999",```sql

    "abc": "A",

    "tipo": 10,-- Performance em login## 📁 Estrutura do Projeto

    "saldo_manut": 50,

    "cmm": 15.0,CREATE NONCLUSTERED INDEX IX_usuarios_email 

    "coef_perda": 0.03

  }'    ON supply_chain.usuarios(email)```



# Ver indicadoresNexum-BackEnd/

curl http://localhost:5000/api/produtos/1/indicadores

-- Performance em busca por matrícula  ├── app.py                      # Aplicação principal Flask

# Produtos críticos

curl http://localhost:5000/api/produtos/necessidade-compra?limit=50CREATE NONCLUSTERED INDEX IX_usuarios_matricula ├── analise_dados.py            # Script de análise de dados

```

    ON supply_chain.usuarios(matricula)├── requirements.txt            # Dependências Python

### JavaScript (Fetch API)

├── .env.example                # Template de configuração

```javascript

// Listar produtos com cobertura baixa-- Performance em filtro por nível├── .gitignore                  # Arquivos ignorados pelo Git

fetch('http://localhost:5000/api/produtos/cobertura-baixa?meses=3')

  .then(res => res.json())CREATE NONCLUSTERED INDEX IX_usuarios_nivel_acesso │

  .then(data => {

    console.log(`${data.total} produtos com cobertura < 3 meses`);    ON supply_chain.usuarios(nivel_acesso)├── database/                   # Scripts e docs do banco de dados

    data.produtos.forEach(p => {

      console.log(`${p.codigo}: ${p.indicadores.cobertura_meses} meses`);```│   ├── create_table.sql        # Criação de tabelas, views, SPs

    });

  });│   ├── insert_data.py          # Script Python para inserção



// Criar produto---│   ├── generate_inserts.py     # Gerador de INSERTs SQL

fetch('http://localhost:5000/api/produtos/', {

  method: 'POST',│   ├── insert_data.sql         # INSERTs gerados (não commitado)

  headers: { 'Content-Type': 'application/json' },

  body: JSON.stringify({## 🔐 Sistema de Autenticação│   └── README.md               # Documentação do banco

    codigo: 'MAT-888',

    abc: 'B',│

    tipo: 19,

    saldo_manut: 75,### 🏗️ Arquitetura em Camadas├── dados_hackathon.csv         # Dados de entrada (5.000 produtos)

    cmm: 20.5

  })├── SETUP_DATABASE.md           # Guia de setup do banco

})

.then(res => res.json())```└── README.md                   # Este arquivo

.then(data => console.log('Produto criado:', data));

```┌─────────────────────────────────────────────────────────────┐```



---│                    CLIENT (Frontend/Postman)                │



## 📖 Documentação Swagger└──────────────────────┬──────────────────────────────────────┘---



Acesse a documentação interativa completa em:                       │ HTTP Request (JSON)



**http://localhost:5000/docs**                       ▼## 🗄️ Banco de Dados



- ✅ Todos os endpoints documentados┌─────────────────────────────────────────────────────────────┐

- ✅ Exemplos de request/response

- ✅ Interface "Try it out" para testar│              CONTROLLER (controllers/user_controller.py)     │### **Tabela Principal**

- ✅ Especificação OpenAPI 2.0

│  • Recebe requisições HTTP                                   │`supply_chain.produtos_estoque` - Controle completo de estoque

Para ver apenas a especificação JSON:

│  • Valida dados de entrada                                   │

**http://localhost:5000/swagger.json**

│  • Retorna respostas JSON                                    │### **Views Disponíveis**

---

└──────────────────────┬──────────────────────────────────────┘1. `vw_produtos_criticos` - Produtos com risco de ruptura

## 📝 FAQ

                       │ Chama Service2. `vw_dashboard_executivo` - KPIs gerenciais

### **1. O que são "peças boas"?**

Peças disponíveis no Manut para uso pelo CAT, incluindo saldo_manut, provid_compras, recebimento_esperado, etc.                       ▼3. `vw_analise_abc` - Análise por classificação



### **2. Como funciona o cálculo de CMM?**┌─────────────────────────────────────────────────────────────┐

CMM = Total consumido nos últimos 6 meses / 6

│               SERVICE (services/user_service.py)             │### **Stored Procedures**

### **3. O que é o Coeficiente de Perda?**

Percentual histórico de peças que não puderam ser reparadas.│  • Validações de negócio                                     │1. `sp_calcular_necessidade_compra` - Cálculo inteligente de compras



### **4. Por que o saldo total difere por tipo?**│  • Hash de senha (bcrypt)                                    │

- **T-10/T-19**: Inclui peças em reparo (podem voltar)

- **T-20**: Apenas peças boas (descartáveis não retornam)│  • Lógica de autenticação                                    │### **Queries Úteis**



### **5. Como interpretar o QA?**└──────────────────────┬──────────────────────────────────────┘

- **QA = 0**: Estoque suficiente

- **QA > 0**: Quantidade que deve ser comprada imediatamente                       │ Chama Repository```sql



### **6. O que é o Fator de Ajuste (FA)?**                       ▼-- Ver produtos críticos

Ponto de pedido que considera estoque de segurança + leadtime + perdas

┌─────────────────────────────────────────────────────────────┐SELECT * FROM supply_chain.vw_produtos_criticos

### **7. Como funciona a cobertura?**

Indica quantos meses o estoque atual dura com base no CMM│          REPOSITORY (repositories/user_repository.py)        │WHERE nivel_criticidade = 'CRÍTICO';



---│  • Queries SQL                                               │



## 🚀 Roadmap│  • CRUD no banco de dados                                    │-- Calcular necessidade de compra (30 dias, fator 1.5)



- [ ] Histórico de consumo (tabela separada)│  • Conversão User ↔ Database                                 │EXEC supply_chain.sp_calcular_necessidade_compra 

- [ ] Integração com ERP

- [ ] Alertas via e-mail/webhook└──────────────────────┬──────────────────────────────────────┘  @lead_time_dias = 30,

- [ ] Dashboard em tempo real

- [ ] Previsão de demanda com ML                       │ PyODBC  @fator_seguranca = 1.5;

- [ ] Relatórios em PDF

- [ ] Auditoria completa de ações                       ▼



---┌─────────────────────────────────────────────────────────────┐-- Dashboard executivo



## 👥 Equipe BBTS-Nexum│              DATABASE (Azure SQL - supply_chain.usuarios)    │SELECT * FROM supply_chain.vw_dashboard_executivo;



Desenvolvido com ❤️ para o Hackathon Stefanini 2025└─────────────────────────────────────────────────────────────┘```



---```



## 📄 Licença📖 **Documentação completa:** [database/README.md](database/README.md)



MIT License - Veja [LICENSE](LICENSE) para mais detalhes### 🔒 Segurança



------



**🔗 Links Úteis:**#### Hash de Senhas (bcrypt)

- Repositório: https://github.com/BBTS-Nexum/Nexum-BackEnd

- Documentação Swagger: http://localhost:5000/docs## 🔧 Tecnologias

- Especificação OpenAPI: http://localhost:5000/swagger.json

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
