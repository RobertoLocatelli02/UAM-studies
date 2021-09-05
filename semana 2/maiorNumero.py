while True:
    try:
        numero1 = float(input('Informe um número:\n'))
        numero2 = float(input('Informe um outro número:\n'))
        if numero1 > numero2:
            print(f'{numero1} > {numero2}')
        elif numero1 < numero2:
            print(f'{numero2} > {numero1}')
        else:
            print(f'{numero1} = {numero2}')
        break
    except ValueError:
        print('Valor inserido não é válido! Insira um valor numérico.')