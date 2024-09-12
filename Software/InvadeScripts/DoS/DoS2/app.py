from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Bem-vindo ao site vulnerável!"

@app.route('/processamento', methods=['POST'])
def processamento():
    data = request.get_json()
    if 'dados' not in data:
        return jsonify({'error': 'Dados ausentes'}), 400

    dados = data['dados']

    # Simulação de processamento intensivo
    for _ in range(1000000):
        dados = dados.upper()

    return jsonify({'resultado': dados})

if __name__ == '__main__':
    app.run(debug=True)


#app = Flask(__name__)

#if __name__ == '__main__':
#    app.run()