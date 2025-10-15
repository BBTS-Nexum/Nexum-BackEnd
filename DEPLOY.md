# 🚀 Deploy no Vercel

## Passo a Passo

### 1. Instalar Vercel CLI

```bash
npm install -g vercel
```

### 2. Login no Vercel

```bash
vercel login
```

### 3. Configurar Variáveis de Ambiente

No dashboard do Vercel, adicione as variáveis (Settings → Environment Variables):

- `AZURE_SQL_DRIVER` = `ODBC Driver 18 for SQL Server`
- `AZURE_SQL_SERVER` = `cesar-abraao.database.windows.net`
- `AZURE_SQL_PORT` = `1433`
- `AZURE_SQL_DATABASE` = `stefanini_app`
- `AZURE_SQL_USERNAME` = `abraaoadmin`
- `AZURE_SQL_PASSWORD` = `sua-senha-aqui`
- `AZURE_SQL_ENCRYPT` = `yes`
- `AZURE_SQL_TRUST_SERVER_CERTIFICATE` = `no`
- `AZURE_SQL_CONNECTION_TIMEOUT` = `30`

**⚠️ IMPORTANTE:** Não commite o arquivo `.env` com senhas reais!

### 4. Deploy

```bash
vercel --prod
```

## Estrutura do Projeto

```
Nexum-BackEnd/
├── api/                        # Código da aplicação
│   ├── index.py               # Entry point (Flask app)
│   ├── controllers/           # Rotas da API
│   ├── services/              # Lógica de negócio
│   ├── repositories/          # Acesso a dados
│   ├── models/                # Modelos de dados
│   └── database/              # Scripts SQL
├── vercel.json                # Configuração Vercel
├── .vercelignore              # Arquivos ignorados
├── requirements.txt           # Dependências Python
└── swagger.json               # Documentação OpenAPI
```

## Comandos Úteis

```bash
# Deploy de preview
vercel

# Deploy de produção
vercel --prod

# Ver logs
vercel logs

# Listar deploys
vercel ls
```

## Configuração Local

Para testar localmente após a reorganização:

```bash
python api/index.py
```

Acesse: http://localhost:5000/docs
