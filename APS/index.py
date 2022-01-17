from random import seed
from random import randint
import time
import sys
import numpy as np
import pandas
import matplotlib.pyplot as plt

sys.setrecursionlimit(10 ** 9)


def partition(colecao, low, high):
    i = (low - 1)        
    pivot = colecao[high]    

    for j in range(low, high):
        if colecao[j] <= pivot:
            i += 1
            colecao[i], colecao[j] = colecao[j], colecao[i]

    colecao[i + 1], colecao[high] = colecao[high], colecao[i + 1]
    return (i + 1)


def quickSortIterative(colecao, l, h):
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
        p = partition( colecao, l, h )

        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


def quickSortRecursive(colecao, low, high):
    if low < high:
        pi = partition(colecao, low, high)
        quickSortRecursive(colecao, low, pi-1)
        quickSortRecursive(colecao, pi + 1, high)


def criarColecao(colecao, tamanho):
    for indice in range(0, tamanho):
        valor = np.int64(randint(0, 51))
        colecao.append(valor)


def main():
    #TAMANHOS = [ 1, 50, 500, 1000, 5000, 10000, 15000 ]
    TAMANHO = 15000
    colecao = []

    criarColecao(colecao,  TAMANHO)

    colecaoRecursiva = colecao.copy()
    colecaoIterativa = colecao.copy()

    tempoInicial = time.time() 
    quickSortRecursive(colecaoRecursiva, 0, TAMANHO - 1)
    tempoFinal = time.time()
    tempoSolucaoRecursiva = tempoFinal - tempoInicial
    print("Tempo Solução Recursiva: {} s".format(tempoFinal - tempoInicial))

    tempoInicial = time.time() 
    quickSortIterative(colecaoIterativa, 0, TAMANHO - 1) 
    tempoFinal = time.time()
    tempoSolucaoIterativa = tempoFinal - tempoInicial
    print("Tempo Solução Iterativa: {} s".format(tempoFinal - tempoInicial))

    dados = {
        "TAMANHO": [TAMANHO],
        "TEMPO_SOLUCAO_RECURSIVA": tempoSolucaoRecursiva,
        "TEMPO_SOLUCAO_ITERATIVA": tempoSolucaoIterativa
    }

    try:
        planilhaAntiga = pandas.read_excel("dados.xlsx")
        planilhaNova = pandas.DataFrame.from_dict(dados)
        planilhaNova = pandas.concat([planilhaAntiga, planilhaNova])
        planilhaNova.to_excel("dados.xlsx", index = False)
    except:
        planilhaNova = pandas.DataFrame.from_dict(dados)
        planilhaNova.to_excel("dados.xlsx", index = False)
    finally:
        planilha = pandas.read_excel("dados.xlsx")
        planilhaSorted = planilha.sort_values(["TAMANHO"])

        plt.plot(planilhaSorted["TAMANHO"], planilhaSorted["TEMPO_SOLUCAO_RECURSIVA"],  color = "purple", label = "Tempo Recursiva")
        plt.plot(planilhaSorted["TAMANHO"], planilhaSorted["TEMPO_SOLUCAO_ITERATIVA"],  color = "yellow", label = "Tempo Iterativa")
        plt.title("Tamanho da coleção x Tempo de solução")
        plt.xlabel("Tamanho")
        plt.ylabel("Tempo")
        plt.legend()
        plt.legend()
        plt.savefig("terceiraTentativa.png")
        plt.show()


if __name__ == "__main__":
    main()