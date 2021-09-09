def pegaNomeCompletoComPrint(nome, sobrenome):
    print(f'NOME COMPLETO: {nome} {sobrenome}')

#pegaNomeCompletoComPrint("Roberto", "Locatelli")


def pegaNomeCompletoComRetorno(nome, sobrenome):
    return f'NOME COMPLETO: {nome} {sobrenome}'

"""print(pegaNomeCompletoComRetorno("Roberto", "Locatelli"))
#OU
resultado = pegaNomeCompletoComRetorno("Roberto", "Locatelli")
print(resultado)"""

def main():
    pegaNomeCompletoComPrint("Roberto", "Locatelli")

if __name__ == "__main__":
    main()
