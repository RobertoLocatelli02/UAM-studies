from math import pi

def areaCirculo(raio):
    return pi * (raio ** 2)

def perimetroCirculo(raio):
    return pi * 2 * raio

def main():
    raio = int(input("Digite o raio do círculo: "))
    print(f'Área do círculo: {areaCirculo(raio)}')
    print(f'Perímetro do círculo: {perimetroCirculo(raio)}')

if __name__ == "__main__":
    main()