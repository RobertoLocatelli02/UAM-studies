def verificaValorComPrint(numero):
    if numero > 0:
        print(f'{numero} É POSITIVO')
    elif numero < 0:
        print(f'{numero} É NEGATIVO\nTRANSOFRMANDO PARA POSITIVO FICARA: {numero * -1}')
    else:
        print(f'{numero} É NULO')

verificaValorComPrint(9)


def verificaValorComRetorno(numero):
    if numero > 0:
        return f"{numero} É POSITIVO"
    elif numero < 0:
        return f"{numero} É NEGATIVO\nTRANSFORMANDO PARA POSITIVO FICARÁ: {numero * -1}"
    else:
        return f"{numero} É NULO"

print(verificaValorComRetorno(9))
#OU
resultado = verificaValorComRetorno(9)
print(resultado)