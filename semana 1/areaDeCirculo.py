from math import pi

while True:
    try:
        raio = float(input('Qual o raio do circulo?\n'))
        if raio > 0:
            print(f'{pi} * {raio}² = {round(pi * (raio ** 2),7)}')
            break
        else:
            print('Valor inserido não é válido! Raio do círculo tem que ser maior que zero.')
    except ValueError:
        print('Valor inserido não é válido!')