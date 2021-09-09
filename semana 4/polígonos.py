def definicaoPoligonos(quantLados):
    if quantLados == 3:
        print(f'TRIÂNGULO')
    elif quantLados == 4:
        print(f'QUADRADO')
    elif quantLados == 5:
        print(f'PENTAGONO')
    else:
        print('VALOR INVÁLIDO')

def main():
    lados = int(input("Digite a quantidade de lados do polígono: "))
    definicaoPoligonos(lados)

if __name__ == "__main__":
    main()