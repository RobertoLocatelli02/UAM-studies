def resultadoValor(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def main():
    numero = int(input("Digite um número: "))
    print(resultadoValor(numero))

if __name__ == "__main__":
    main()