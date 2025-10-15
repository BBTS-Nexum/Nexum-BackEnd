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

No dashboard do Vercel, adicione as variáveis:

- `DB_SERVER` - Servidor Azure SQL
- `DB_DATABASE` - Nome do banco
- `DB_USERNAME` - Usuário do banco
- `DB_PASSWORD` - Senha do banco

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
