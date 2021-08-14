import math

while True:
    try:
        cateto1 = float(input('Informe o primeiro cateto do triângulo retângulo:\n'))
        if cateto1 <= 0:
            print('Valor inserido não é valido. Cateto tem que ser maior que zero')
        else:
            cateto2 = float(input('Agora o segundo cateto:\n'))
            if cateto2 <= 0:
                print('Valor inserido não é valido. Cateto tem que ser maior que zero')
            else:
                print(f'A hipotenusa equivale à {math.pow((math.pow(cateto1,2) + math.pow(cateto2,2)),1/2)}')
                break
    except ValueError:
        print('Valor inserido não é válido!')