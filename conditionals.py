def run():
    age = int(input('Ingrese su edad: '))
    # Esto es un comentario
    if age > 18:
        print('Eres mayor de edad')
    else:
        print('Eres menor de edad')

    if age > 20:
        print('La edad ingresada es mayor a 20')
    elif age < 20:
        print('La edad ingresada es menor a 20')
    else:
        print('La edad ingresada es 20')


if __name__ == '__main__':
    run()
