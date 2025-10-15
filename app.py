""""""

Nexum Supply Chain APIEntry point para Vercel

Entry point para VercelImporta a aplicação Flask de api/index.py

""""""

from api.index import appfrom api.index import app



# Vercel procura pela variável 'app'# Vercel procura por uma variável 'app' neste arquivo

if __name__ == "__main__":if __name__ == "__main__":

    app.run()    app.run()


    print('NEXUM SUPPLY CHAIN API'.center(80))
    print('='*80)
    print('\nServidor: http://localhost:5000')
    print('Documentação: http://localhost:5000/docs\n')
    print('='*80 + '\n')
    app.run(debug=True, host='0.0.0.0', port=5000)
