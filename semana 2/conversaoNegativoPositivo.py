while True:
    try:
        numero = float(input('Informe um número:\n'))
        if numero < 0:
            print(f'{numero} é negativo \nApós a conversão ficará: {numero - (2 * numero)}')
        else:
            print(f'{numero} é positivo')
        break
    except ValueError:
        print('Valor inserido não é válido! Insira um valor numérico.')