def separarPalavra(palavra, contador):
    if contador < len(palavra):
        print(palavra[contador])
        separarPalavra(palavra, contador + 1)

palavra = input("Digite uma palavra: ")

separarPalavra(palavra, 0)
