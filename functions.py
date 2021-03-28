def imprimir_mensaje1():
    print('Aprendiendo el uso de funciones con Python')


def imprimir_mensaje(option):
    # La siguiente línea de código se debe a que quiero concatenar y solo es posible con los strings
    option = str(option)
    print('Holaa!!!')
    print('Elegiste la opción ' + option)
    print('Adios')


def run():
    imprimir_mensaje1()
    imprimir_mensaje1()
    imprimir_mensaje1()
    print('Bienvenido al programa para elegir opciones: ')

    # Uso de parámetros
    option = int(input('Elige una opción: 1, 2 o 3: '))
    if option == 1:
        imprimir_mensaje(1)
    elif option == 2:
        imprimir_mensaje(2)
    elif option == 3:
        imprimir_mensaje(3)
    else:
        print('Debes elegir una opción válida')
        print('***Fin del programa***')


if __name__ == '__main__':
    run()
