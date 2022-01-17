import pandas as pd

listaNomes = ["Vingadores: Guerra Infinita", "Vingadores", "Vingadores: A Era de Ultron", "Pantera Negra", "Homem de Ferro 3"]
listaBilheterias = ["1,82 bilhão", "1,51 bilhão", "1,40 bilhão", "1,34 bilhão", "1,21 bilhão"]
listaColocacaoMundial = ["4°", "6°", "8°", "9°", "15°"]

dados = {
    "NOME": listaNomes,
    "BILHETERIA": listaBilheterias,
    "POSICAO_MUNDIAL": listaColocacaoMundial
}

dadosDF = pd.DataFrame.from_dict(dados)
dadosDF.to_excel("./semana 7/bilheteria.xlsx")