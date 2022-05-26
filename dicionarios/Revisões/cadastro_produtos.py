products = {}


def addProduct(product, value):
    products[product] = value
    print("\nProduto adicionado com sucesso!")


def searchProduct(product):
    if len(products) == 0:
        print("\nNão há produtos, adicione primeiro!")
    else:
        result = products.get(product, 0)
        if result == 0:
            print("\nProduto não encontrado!")
        else:
            print("\nProduto:", product, "\nValor:", result)


def removeProduct(product):
    if len(products) == 0:
        print("\nNão há produtos, adicione primeiro!")
    else:
        result = products.get(product, 0)
        if result == 0:
            print("\nProduto não encontrado")
        else:
            products.pop(product)
            print("\nProduto removido com sucesso!")


def printProduct(dicionario):
    if len(products) == 0:
        print("\nNão há produtos, adicione primeiro!")
    else:
        for key, value in dicionario.items():
            print("[ Produto: ", key, ", Valor: ", value, " ]", sep="")


controlVar = -1
while controlVar != 0:
    print(
        "\nDigite 1 para adicionar novo produto;\nDigite 2 para listar todos os produtos;\nDigite 3 para pesquisar produto;\nDigite 4 para remover produto;\nDigite 0 para sair;")

    controlVar = int(input())

    if controlVar == 1:
        newProductName = input("\nDigite o nome do novo produto: ")
        newProductvalue = input("\nDigite o valor do novo produto: ")
        addProduct(newProductName, newProductvalue)

    if controlVar == 2:
        printProduct(products)

    if controlVar == 3:
        productName = input("\nDigite o nome do produto a ser pesquisado: ")
        searchProduct(productName)

    if controlVar == 4:
        productName = input("\nDigite o nome do produto a ser removido: ")
        removeProduct(productName)