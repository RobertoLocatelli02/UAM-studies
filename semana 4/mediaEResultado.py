def calculaMedia(nota1, nota2):
    return (nota1 + nota2) / 2

def resultado(media):
    if media >= 6:
        return f"VOCÊ FOI APROVADO COM MÉDIA {media}"
    else:
        return f"VOCÊ FOI REPROVADO COM MÉDIA {media}"

def notaValida():
    while True:
        nota = float(input("Digite a nota da prova: "))
        if nota >= 0 and nota <= 10:
            break
    return nota

def main():
    nota1 = notaValida()
    nota2 = notaValida()
    media = calculaMedia(nota1, nota2)
    print(resultado(media))

if __name__ == "__main__":
    main()