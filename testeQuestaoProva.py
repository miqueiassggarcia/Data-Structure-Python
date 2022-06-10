from random import randint

def numeroVencedores(lista):
    vencedores = {}
    for i in lista:
        vencedores[i] = vencedores.get(i, 0) + 1

    vencedor = [-1, -1]

    for key, value in vencedores.items():
        if value > vencedor[1]:
            vencedor[0] = key
            vencedor[1] = value

    return vencedor

lista = []

for i in range((15)):
    lista.append(randint(0,9))

print(lista)

print(numeroVencedores(lista))
