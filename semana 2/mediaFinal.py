while True:
    try:
        nota1 = float(input("Informe a primeira nota:\n"))
        if nota1 < 0 or nota1 > 10:
            print('Por favor, insira um valor entre 0 e 10')
        else:
            nota2 = float(input("Agora a segunda nota:\n"))
            if nota2 < 0 or nota2 > 10:
                print('Por favor, insira um valor entre 0 e 10')
            else:
                nota3 = float(input("Agora a terceira nota:\n"))
                if nota3 < 0 or nota3 > 10:
                    print('Por favor, insira uma valor entre 0 e 10')
                else:
                    mediaFinal = ((nota1 + nota2 + nota3) / 3)
                    if mediaFinal >= 6:
                        aprovado = True
                    else:
                        aprovado = False
                    print(aprovado)
                    break
    except ValueError:
        print("Valor inserido não é válido! Por favor insira um valor numérico entre zero e dez.")
