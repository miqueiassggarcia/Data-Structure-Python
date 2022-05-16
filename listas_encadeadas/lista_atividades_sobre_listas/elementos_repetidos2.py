from listas_encadeadas.lista_encadeada import LinkedList

def valoresRepetidos(list):
    ocorrencias = {}
    for i in range(list.getSize()):
        ocorrencias[list[i]] = ocorrencias.get(list[i], 0) + 1

    return ocorrencias


list = LinkedList()

list.preencherAleatoriamente(25)

print("Lista completa:", list)

valoresRepetidos = valoresRepetidos(list)

print("Valores repetidos: ", end="")
for key, value in valoresRepetidos.items():
    if value > 1:
        print(key, end=" ")
