def votacion_function():
    N = int(input())
    index = 0
    max = 0
    winner = ''
    votos = []
    lista_de_candidatos = []
    while index < N:
        nombre_candidato = input().upper()
        if nombre_candidato in lista_de_candidatos:
            votos[lista_de_candidatos.index(nombre_candidato)] = votos[lista_de_candidatos.index(nombre_candidato)] + 1
        else:
            lista_de_candidatos.append(nombre_candidato)
            votos.append(1)
        index += 1
    max = max(lista_de_candidatos)
    winner = lista_de_candidatos(index(max))
    print(winner)


def run():
    votacion_function()


if __name__ == '__main__':
    run()