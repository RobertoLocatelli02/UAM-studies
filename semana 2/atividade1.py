import random

portal = random.randint(1, 5)
caminho_vermelho = 1
caminho_preto = 2
sala = 1
cont = 1

caminho = int(input("""Você está no início!
Escolha seu caminho:
[ 1 ] caminho vermelho
[ 2 ] caminho preto\n"""))

while sala + caminho <= 8 and cont <= 7:

    if caminho == 2 and sala == 4 or caminho == 1 and sala == 5:
        print("Você esta na sala : 6  \nVocê será redirecionado para a sala 8")
        sala = portal
        print(f"O portal te jogara para a sala {portal}")
        cont += 1
        sala -= caminho
    elif (caminho == 1):
        print("Você esta na sala: {}".format(sala + caminho_vermelho))
        print("Escolha seu caminho: ")
        print("[1] caminho vermelho")
        print("[2] caminho preto")
        sala = sala + caminho_vermelho
        caminho = int(input())
        cont += 1
    else:
        print("Você esta na sala: {}".format(sala + caminho_preto))
        print("Escolha seu caminho: ")
        print("[1] caminho vermelho")
        print("[2] caminho preto")
        sala = sala + caminho_preto
        caminho = int(input())
        cont += 1
sala += caminho

if (sala >= 9):
    print("Você esta na sala : 9")
    print("VENCEU !!!!!!")
else:
    print("Você não chegou na sala 9 \nGAME OVER!!")