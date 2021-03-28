# MÉTODOS
# upper() --> convierte a mayúsucla
# capitalize --> convierte a mayúscula la primera letra de la palabra
# strip() --> elimina los espacios que están de más
# lower() --> convierte a minúscula
# replace('a', 'b') --> reemplaza todas las letras 'a' de la cadena por la letra 'b'
# Índices --> si nombre == 'Marcos' ENTONCES: nombre[0] --> 'm'
# len() --> devuelve el número de caracteres de la cadena de texto
# Slice --> cortar cadenas de caracteres

def run():
    name = input('Ingrese su nombre: ')

    print('Su nombre en mayúsculas: ' + name.upper())
    print('Su nombre en minúsuculas: ' + name.lower())
    print('Su nombre escrito de forma correcta: ' + name.capitalize())
    print('Cantidad de caracteres que quedaron luego de haber utilizado el método capitalize: ' + str(len(name)))
    print('El caracter de la posición 3 en su nombre es: ' + name[2])
    sentence = input('Escriba una oración terminada en un punto: ')

    print('Cambiando las letras o por la letra "e" en su oración: ' +
          sentence.replace('o', 'e'))
    print('La cantidad de caracteres en la frase ingresada es de: ' +
          str(len(sentence)))

    print('\n' + '*** STRIP ***')
    random_word = input(
        'Escriba una palabra con uno o más espacios al final: ')
    print('Cantidad de caracteres de la cadena ingresada: ' + str(len(random_word)))
    print('Cantidad de caracteres sin los espacios sobrantes: ' +
          str(len(random_word.strip())))

    print('\n' + '*** SLICE ***')
    first_name = input('Ingrese su primer nombre: ')
    print('Estas son las primeras 3 letras de su nombre: ' +
          first_name[0:3])  # alternativa: fisrt_name[:3]
    print('Estas son las últimas letras que restan de su nombre:' +
          first_name[3:])
    print('Esta es una secuencia de letras de su nombre: ' + first_name[1:4])

    aux = "PROGRAMACION"
    print('\n' + aux)
    print('Caracteres de la palabra PROGRAMACION, desde la r hasta la o, saltando 2 caracteres: ' +
          aux[1:10:2])

    print('Invertir la palabra PROGRAMACION')
    print(aux[::-1])


if __name__ == '__main__':
    run()
