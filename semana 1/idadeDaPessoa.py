while True:
    try:
        idadeEmAnos = int(input('Informe sua idade: \n'))
        if idadeEmAnos < 0:
            print('Idade inválida! Tente novamente.')
        else:
            print(f'{idadeEmAnos} anos tem aproximadamente {idadeEmAnos * 365} dias \nE {idadeEmAnos} anos tem aproximadamente {idadeEmAnos * 12} meses')
            break
    except ValueError:
        print('Valor inserido não é valido! Tente novamente.')