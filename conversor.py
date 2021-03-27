menu = """
Bienvenido al conversor de moneda

1. Peso colombiano
2. Peso argentino
3. Peso mexicano

Elige una opción: """

option = int(input(menu))

if option == 1:
    pesos = input('Cuántos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 3875
    equivalente_en_dolares = pesos / valor_dolar
    equivalente_en_dolares = round(equivalente_en_dolares, 2)
    equivalente_en_dolares = str(equivalente_en_dolares)
    print('Tienes $' + equivalente_en_dolares + ' dólares')
elif option == 2:
    pesos = input('Cuántos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 50.55
    equivalente_en_dolares = pesos / valor_dolar
    equivalente_en_dolares = round(equivalente_en_dolares, 2)
    equivalente_en_dolares = str(equivalente_en_dolares)
    print('Tienes $' + equivalente_en_dolares + ' dólares')
elif option == 3:
    pesos = input('Cuántos tienes?: ')
    pesos = float(pesos)
    valor_dolar = 21.14
    equivalente_en_dolares = pesos / valor_dolar
    equivalente_en_dolares = round(equivalente_en_dolares, 2)
    equivalente_en_dolares = str(equivalente_en_dolares)
    print('Tienes $' + equivalente_en_dolares + ' dólares')
else:
    print("Ejecute de nuevo el programa y elija una opción válida.")
