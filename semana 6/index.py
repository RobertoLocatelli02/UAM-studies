import os

caminho = 'C:/Users/rloca/Desktop/UAM/1 semestre/técnicas de programação/semana 6'

"""
for (root,dirs,files) in os.walk(caminho, topdown = True): 
    if "script.js" in files:
        print("ACHEEEEEIIII")
"""




diretorio = os.walk(caminho, topdown = True)
print(diretorio)