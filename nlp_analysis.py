# nlp_analysis.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def extrair_palavras_chave(texto):
    nltk.download('punkt')
    nltk.download('stopwords')
    palavras = word_tokenize(texto)
    stop_words = set(stopwords.words('english'))  # ou 'portuguese'
    palavras_filtradas = [palavra for palavra in palavras if palavra.lower() not in stop_words]
    frequencia = FreqDist(palavras_filtradas)
    return frequencia.most_common(10)
