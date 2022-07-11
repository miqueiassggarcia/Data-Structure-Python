def rotacionar_palavra(palavra, chave):
    rotacionada = ""
    for i in palavra:
        aux = ord(i) + chave
        if aux < ord("a"):
            aux += 26
        if aux > ord("z"):
            aux -= 26
        rotacionada += chr(aux)
    return rotacionada


def criptografar(frase, chave):
    palavras = frase.lower().split()
    frase_rotacionada = ""
    for palavra in palavras:
        frase_rotacionada += rotacionar_palavra(palavra, chave) + " "
    return frase_rotacionada


def descriptografar(frase, chave):
    palavras = frase.lower().split()
    frase_original = ""
    for palavra in palavras:
        frase_original += rotacionar_palavra(palavra, chave * (-1)) + " "
    return frase_original


frase_criptografada = criptografar("Um teste", 5)
frase_descriptografada = descriptografar(frase_criptografada, 5)

print(frase_criptografada)
print(frase_descriptografada)
