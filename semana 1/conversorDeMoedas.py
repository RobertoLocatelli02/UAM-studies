while True:
    try:
        valorEmReais = float(input('Informe o valor: \nR$'))
        if valorEmReais >= 0:
            print(f'R${valorEmReais} equivale a: \nU${valorEmReais / 5.25} dólar \nBTC{valorEmReais / 234415.00} bitcoin \n€{valorEmReais / 6.15} euro')
            break
        else:
            print('Valor inserido não é válido! O valor em reais deve ser maior ou igual à zero.')
    except ValueError:
        print('Valor inserido não é válido!')