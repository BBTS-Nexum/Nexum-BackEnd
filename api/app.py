from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from api.controllers.user_controller import user_bp
from api.controllers.produto_controller import produto_bp

app = Flask(__name__)
CORS(app)

# Configuração do Swagger UI
SWAGGER_URL = '/docs'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Nexum Supply Chain API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(user_bp)
app.register_blueprint(produto_bp)

@app.route('/swagger.json')
def swagger_spec():
    """Serve a especificação OpenAPI"""
    import os
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return send_from_directory(root_dir, 'swagger.json')

@app.route('/')
def home():
    return jsonify({
        'message': 'Nexum Supply Chain API',
        'version': '1.0.0',
        'docs': '/docs',
        'spec': '/swagger.json'
    })

# Handler para Vercel
handler = app

if __name__ == '__main__':
    print('\n' + '='*80)
    print('NEXUM SUPPLY CHAIN API'.center(80))
    print('='*80)
    print('\nServidor: http://localhost:5000')
    print('Documentação: http://localhost:5000/docs\n')
    print('='*80 + '\n')
    app.run(debug=True, host='0.0.0.0', port=5000)
