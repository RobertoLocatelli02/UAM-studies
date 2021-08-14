import math

while True:
    try:
        velocidadeInicial = float(input('informe a velocidade inicial do corpo:\n'))
        distanciaPercorrida = float(input('informe a distância percorrida pelo corpo:\n'))
        aceleracao = float(input('informe a aceleração do corpo:\n'))
        if aceleracao == 0.0:
            print('Valor inserido não é válido! Aceleração tem que ser diferente de zero.')
        else:
            print(f'V² = Vo² + 2 * a * ΔS \nV² = {velocidadeInicial}² + 2 * {aceleracao} * {distanciaPercorrida} \nVelocidade final do corpo = {round(math.pow((math.pow(velocidadeInicial,2) + 2 * aceleracao * distanciaPercorrida),1/2),2)} m/s')
            break
    except ValueError:
        print('Valor inserido não é válido.')
        