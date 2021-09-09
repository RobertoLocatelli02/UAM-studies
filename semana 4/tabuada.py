def lerNumero():
    numero = int(input("Digite um número: "))
    return numero

def tabuada(numero):
    for i in range(11):
        print(f'{numero} X {i} = {numero * i}')

def main():
    numero = lerNumero()
    tabuada(numero)

if __name__ == "__main__":
    main()