from listas_encadeadas.lista_encadeada import LinkedList

def valoresRepetidos(list):
    valoresRepetidos = LinkedList()
    for i in range(list.getSize()):
        value = list[i]
        for j in range(list.getSize()):
            if value == list[j] and i != j:
                if not(valoresRepetidos.seachItem(value)):
                    valoresRepetidos.append(value)

    return valoresRepetidos


list = LinkedList()

list.preencherAleatoriamente(10)

print("Lista completa:", list)

valoresRepetidos = valoresRepetidos(list)

if valoresRepetidos.getHead() == None:
    print("\nNão há valores repetidos")
else:
    print("\nValores que se repetem:", valoresRepetidos)
