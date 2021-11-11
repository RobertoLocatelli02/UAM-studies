import pandas as pd


nomes = ["Roberto", "André", "Gabriel", "Daniel"]
idades = [19, 30, 24, 23]
cores = ["Vermelho", "Rosa", "Verde", "Azul"]

informacoes = {
    "NOME": nomes,
    "IDADE": idades,
    "COR_FAVORITA": cores
}

informacoesDF = pd.DataFrame.from_dict(informacoes)

#print(informacoesDF)

try:
    informacoesDF.to_excel('./semana 7/index.xlsx')
except PermissionError:
    print('Erro! O arquivo está aberto.')
else:
    print('Arquivo criado com sucesso')