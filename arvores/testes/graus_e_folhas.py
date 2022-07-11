from arvores.arvore import BSTNode

tree = BSTNode()

values = [20, 33, 9, 18, 41, 26, 3, 12, 29, 10, 44, 45, 42]

for value in values:
    tree.insert(value)

tree.imprimir_graus()

print("Quantidades de folhas:",tree.imprimir_folhas())
