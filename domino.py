def calcularCantidadDeFichas(valorEntero):
    suma = 1
    for index in range(0, valorEntero + 1):
        suma += index
    return valorEntero + suma


def run():
    print("*** CREANDO SU JUEGO DE DOMINO ***\n")
    n = int(input("Defina el mayor valor posible para su juego de domino: "))
    print("\nLa cantidad maxima de fichas sin repetir que tendra su juego es de: " + str(calcularCantidadDeFichas(n)))


if __name__ == '__main__':
    run()