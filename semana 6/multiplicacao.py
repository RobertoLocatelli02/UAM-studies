def multiplicacao(num1, num2):
    if num2 == 1:
        return num1
    return num1 + multiplicacao(num1, num2 - 1)

def main():
    while True:
        try:
            numero1 = int(input("Informe o primeiro número inteiro: "))
            numero2 = int(input("Informe o segundo número inteiro: "))
        except ValueError:
            print("Informe um valor numérico inteiro!")
        else:
            print(multiplicacao(numero1, numero2))
            break


if __name__ == "__main__":
    main()