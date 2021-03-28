# Es importante tener declarada o definida la función antes de ejecutarla
# Es decir, se define y se usa en las líneas siguientes (no arriba)

def conversor(exchange_rate, dollar_value):
    pesos = input('Cuántos pesos ' + exchange_rate + ' tienes?: ')
    pesos = float(pesos)
    dollar = pesos / dollar_value
    dollar = round(dollar, 2)
    dollar = str(dollar)
    print('Tienes $' + dollar + ' dólares')


def run():
    menu = """
    Bienvenido al conversor de moneda

    1. Peso colombiano
    2. Peso argentino
    3. Peso mexicano

    Elige una opción: """

    option = int(input(menu))

    if option == 1:
        conversor('Colombianos', 3875)
    elif option == 2:
        conversor('Argentinos', 79.5)
    elif option == 3:
        conversor('Mexicanos', 45.14)
    else:
        print("Ejecute de nuevo el programa y elija una opción válida.")


if __name__ == '__main__':
    run()
