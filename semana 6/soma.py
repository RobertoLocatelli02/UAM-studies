import time


def somatoria(numero):
    if numero == 1:
        return numero
    return numero + somatoria(numero - 1)


def main():
    inicio = time.time()
    while True:
        try:
            numero = int(input("Informe um número inteiro: "))
        except ValueError:
            print("Numero inserido tem que ser um valor inteiro!")
        else:
            print(somatoria(numero))
            break
    fim = time.time()
    print(f'{fim} - {inicio} = {fim - inicio}')


if __name__ == "__main__":
    main()