pesos = input('Cuántos pesos argentinos tienes?: ')
pesos = float(pesos)

valor_dolar = 50.55
equivalente_en_dolares = pesos / valor_dolar
equivalente_en_dolares = round(equivalente_en_dolares, 2)
equivalente_en_dolares = str(equivalente_en_dolares)
print('Tienes $' + equivalente_en_dolares + ' dólares')
