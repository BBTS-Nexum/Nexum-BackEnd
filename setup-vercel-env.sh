# Configurar Variáveis de Ambiente no Vercel

# Execute esses comandos após fazer 'vercel login'

vercel env add AZURE_SQL_DRIVER production
# Valor: ODBC Driver 18 for SQL Server

vercel env add AZURE_SQL_SERVER production
# Valor: cesar-abraao.database.windows.net

vercel env add AZURE_SQL_PORT production
# Valor: 1433

vercel env add AZURE_SQL_DATABASE production
# Valor: stefanini_app

vercel env add AZURE_SQL_USERNAME production
# Valor: abraaoadmin

vercel env add AZURE_SQL_PASSWORD production
# Valor: [SUA_SENHA]

vercel env add AZURE_SQL_ENCRYPT production
# Valor: yes

vercel env add AZURE_SQL_TRUST_SERVER_CERTIFICATE production
# Valor: no

vercel env add AZURE_SQL_CONNECTION_TIMEOUT production
# Valor: 30
