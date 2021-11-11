import pandas as pd

try:
    informacoesDF = pd.read_excel('./semana 7/index.xlsx')
except FileNotFoundError:
    print('Erro! Arquivo não existe no diretório especificado.')
else:
    print(informacoesDF)