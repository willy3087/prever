from flask import Flask, render_template, request, jsonify
import nlp_analysis  # Importando script NLP
import ml_model  # Importando script de ML
app = Flask(__name__)

# Rota principal que serve a página HTML
@app.route('/')
def home():
    return render_template('index.html')

# Rota para processar a predição
@app.route('/prever', methods=['POST'])
def predicao():
    caminho_csv = '/Users/helbertwilliamduarteteixeira/Desktop/Desk/Logica/js_previsoes/dados_designers_tarefas_atualizado.csv'
    data = request.json
    nome_tarefa = data['nome_tarefa']
    nome_designer = data['nome_designer']
    tempo_estimado = data['tempo_estimado']
    complexidade = data['complexidade']

    # funções de análise NLP e ML para processar os dados recebidos
    resultado_nlp = nlp_analysis.extrair_palavras_chave(nome_tarefa)
    modelo = ml_model.treinar_modelo(caminho_csv, nome_designer)
    entropia_predita = ml_model.prever_entropia(modelo, tempo_estimado, complexidade)

    return jsonify({
        'nome_tarefa': nome_tarefa,
        'resultado_nlp': resultado_nlp,
        'entropia_predita': entropia_predita
    })

if __name__ == '__main__':
    app.run(debug=True)
