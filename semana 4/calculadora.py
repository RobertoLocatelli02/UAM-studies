def menu():
    print("-=" * 30)
    op = int(input("""MENU DE OPÇÕES:
[ 1 ] Adição
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão
[ 5 ] Sair do programa
SUA OPÇÃO: """))
    print("-=" * 30)
    return op

def lerNumero():
    numero = float(input("Digite um número: "))
    return numero

def escolhaDoUsuario(op, numero1, numero2):
    if op == 1:
        return f"{numero1 + numero2:^60}"
    elif op == 2:
        return f"{numero1 - numero2:^60}"
    elif op == 3:
        return f"{numero1 * numero2:^60}"
    elif op == 4:
        return f"{numero1 / numero2:^60}"

def main():
    opcao = menu()
    numero1 = lerNumero()
    numero2 = lerNumero()
    while opcao != 5:
        print(escolhaDoUsuario(opcao, numero1, numero2))
        opcao = menu()

if __name__ == "__main__":
    main()