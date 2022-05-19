def rotacionar_palavra(values, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'
    new_values = ''
    for char in values:
        index = alphabet.find(char)
        if index == -1:
            new_values += char
        else:
            new_index = index + key
            new_index = new_index % len(alphabet)
            new_values += alphabet[new_index:new_index+1]
    return new_values


def rotate_word(values, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_values = ''
    for char in values:
        index = alphabet.find(char)
        if index == -1:
            new_values += char
        else:
            new_index = index + key
            new_index = new_index % len(alphabet)
            new_values += alphabet[new_index:new_index+1]
    return new_values


string = input("Digite uma frase a ser cifrada: ")
key = int(input("Digite a rotacao da cifra: "))

splited_string = string.split()

encrypted_string = ''

for word in splited_string:
    encrypted_string += rotate_word(word, key) + " "

print(encrypted_string)

splited_string = encrypted_string.split()

encrypted_string = ''

for word in splited_string:
    encrypted_string += rotate_word(word, key * (-1)) + " "

print(encrypted_string)
