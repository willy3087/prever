# ml_model.py

import logging
import pandas as pd
from sklearn.linear_model import LinearRegression

def treinar_modelo(caminho_csv, nome_designer):
    logging.info(f"Iniciando treinamento do modelo para o designer {nome_designer}")
    df = pd.read_csv(caminho_csv)
    df_filtrado = df[df['Nome'] == nome_designer]

     # Log das estatísticas básicas
    logging.info(f"Estatísticas dos dados: {df_filtrado.describe()}")

    X = df_filtrado[['Tempo', 'Complexidade']]
    y = df_filtrado['Entropia']
    modelo = LinearRegression().fit(X, y)
    
    logging.info("Modelo treinado com sucesso")
    return modelo

def prever_entropia(modelo, tempo, complexidade):
    dados_predicao = pd.DataFrame({
        'Tempo': [tempo],
        'Complexidade': [complexidade]
    })
    return modelo.predict(dados_predicao)[0]