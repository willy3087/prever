# main.py

import logging
from nlp_analysis import extrair_palavras_chave
from ml_model import treinar_modelo, prever_entropia

# Solicitar informações sobre a próxima tarefa
nome_tarefa = input("Digite o nome da próxima tarefa: ")
#log de entrada do usuário
logging.info(f"Nome da tarefa inserido: {nome_tarefa}")

nome_designer = input("Digite o nome do designer (Designer1, Designer2, Designer3): ")
logging.info(f"Designer escolhido: {nome_designer}")

# Análise NLP do nome da tarefa
palavras_chave = extrair_palavras_chave(nome_tarefa)
print("Palavras-chave da tarefa:", palavras_chave)

# Treinar o modelo para o designer específico
caminho_csv = '/Users/helbertwilliamduarteteixeira/Desktop/Desk/Logica/js_previsoes/dados_designers_tarefas_atualizado.csv'
modelo = treinar_modelo(caminho_csv, nome_designer)

# Fazer uma previsão para a tarefa (valores de exemplo para tempo e complexidade)
tempo_estimado = float(input("Digite o tempo estimado para a tarefa (em horas): "))
complexidade = int(input("Digite a complexidade da tarefa (em uma escala de 1 a 5): "))

entropia_predita = prever_entropia(modelo, tempo_estimado, complexidade)
print(f"A entropia prevista para a tarefa '{nome_tarefa}' é {entropia_predita:.2f}")
