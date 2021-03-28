# Buenas prácticas:
#   Hacer uso de una función principal
#   Dejar dos saltos de línea entre funciones

def palindrome(text):
    # cambio la cadena a minúscula y reemplazo todos los espacios por un vacio
    text = text.lower().replace(' ', '')
    inverted_text = text[::-1]
    if text == inverted_text:
        return True
    else:
        return False


def run():
    text = input('Escribe una palabra o frase: ')
    is_palindrome = palindrome(text)
    if is_palindrome == True:
        print('El texto ingresado es un palíndromo.')
    else:
        print('El texto ingresado no es un palíndromo.')


# entry point
if __name__ == '__main__':
    run()
