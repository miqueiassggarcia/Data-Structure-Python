from listas_encadeadas.lista_encadeada import LinkedList

def buscaBinaria(list, ini, fim, value):
    meio = (ini + fim) // 2

    if list[meio] == value:
        return meio
    elif ini == fim:
        return -1
    elif value > list[meio]:
        return buscaBinaria(list, meio + 1, fim, value)
    else:
        return buscaBinaria(list, ini, meio - 1, value)

    return -1;

list = LinkedList()

list.preencherEmOrdem(100)

print(list)

position = buscaBinaria(list, 0, 100, 100)

print(position)

