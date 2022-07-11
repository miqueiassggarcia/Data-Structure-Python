from arvores.arvore import BSTNode

tree = BSTNode()

values = [20, 33, 9, 18, 41, 26, 3, 12, 29, 10, 44, 45, 42]

for value in values:
    tree.insert(value)

print("\nPre-ordem: ", end="")
tree.print_pre()
print("\nOrdem central: ", end="")
tree.print_central()
print("\nPos-ordem: ", end="")
tree.print_pos()

print('\n\nTotal de nós:', tree.total_nodes())
print('Altura:', tree.altura())
