def trocaDeValoresComPrint(numero1, numero2):
    print(f'NUMERO 1: {numero1}\nNUMERO 2: {numero2}')
    numeroAntigo = numero1
    numero1 = numero2
    numero2 = numeroAntigo
    print(f'APÓS A TROCA:\nNUMERO 1: {numero1}\nNUMERO 2: {numero2}')

trocaDeValoresComPrint(2, 5)

def trocaDeValoresComRetorno(numero1, numero2):
    numeroAntigo1 = numero1
    numeroAntigo2 = numero2
    numero1 = numero2
    numero2 = numeroAntigo1
    return f'''NUMERO 1: {numeroAntigo1}
NUMERO 2: {numeroAntigo2}
APÓS A TROCA:
NUMERO 1: {numero1}
NUMERO 2: {numero2}'''

print(trocaDeValoresComRetorno(2 , 5))
#OU
resultado = trocaDeValoresComRetorno(2, 5)
print(resultado)