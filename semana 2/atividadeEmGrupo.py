try:
    n1a = float(input('Informe sua nota N1A: '))
    if n1a < 0 or n1a > 10:
        print('Insira um valor entre 0 e 10.')
    else:
        n1b = float(input('Informe sua nota N2B: '))
        if n1b < 0 or n1b > 10:
            print('Insira um valor entre 0 e 10.')
        else:
            n2aps = float(input('Informe sua nota N2 APS: '))
            if n2aps < 0 or n2aps > 10:
                print('Insira um valor entre 0 e 10.')
            else:
                n2b = 0

                n1 = n1a * 0.5 + n1b * 0.5
                n2 = n2b * 0.9 + n2aps * 0.1
                mediaFinal = n1 * 0.4 + n2 * 0.6
                notaRestante = (10 * (6 - mediaFinal)) / 5.4

                print(f'O aluno precisa de {round(notaRestante, 2)} na N2')
except ValueError:
    print('Valor inserido é inválido! Insira um valor numérico.')
