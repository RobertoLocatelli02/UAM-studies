while True:
    try:
        numero = int(input("Informe um número:\n"))
        impar = True
        if numero % 2 == 0:
            impar = False
        print(f'O numero {numero} é ímpar: {impar}')
        break
    except ValueError:
        print('Valor inserido não é válido! Por favor insira um número inteiro.')