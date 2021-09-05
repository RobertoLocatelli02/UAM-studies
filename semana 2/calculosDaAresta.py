import math

while True:
    try:
        aresta = float(input('Informe a aresta:\n'))
        print(f'A área do círculo é {math.pi * (aresta ** 2)} e a área do quadrado é {aresta ** 2}. O círculo possuí área maior que a do quadrado? {(math.pi * (aresta ** 2)) > (aresta ** 2)}')
        break
    except ValueError:
        print('Valor inserido não é válido! Insira um valor numérico.')