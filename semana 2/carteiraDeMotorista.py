while True:
    try:
        idade = int(input('Informe sua idade:\n'))
        if idade <= 0:
            print('Idade não pode ser menor ou igual a zero')
        else:
            if idade >= 18:
                print('Você já pode realizar a prova para tirar a carteira de motorista')
            else:
                print('Você ainda não é maior de idade')
            break
    except ValueError:
        print('Valor inserido não é válido! Idade tem que ser um número inteiro')