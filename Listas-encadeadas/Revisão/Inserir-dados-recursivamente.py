def adicionarDados(lista, contador):
    if contador < 4:
        lista.append(input("Digite um valor: "))
        adicionarDados(lista, contador + 1)

lista = []
contador = 0

adicionarDados(lista, contador)

print(lista)