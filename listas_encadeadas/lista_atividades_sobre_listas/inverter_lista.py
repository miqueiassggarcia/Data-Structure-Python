from listas_encadeadas.lista_encadeada import LinkedList
from pilha_e_fila.pilha import Pilha

lista = LinkedList()

lista.preencherAleatoriamente(10)

print("Lista na ordem normal:", lista)

pilha = Pilha()

for i in range(10):
    pilha.push(lista[i])

listaInversa = LinkedList()

while not pilha.isEmpty():
    listaInversa.append(pilha.pop())

print("Lista na ordem inversa:", listaInversa)
