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
            new_values += alphabet[new_index]
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
            new_values += alphabet[new_index]
    return new_values


string = input("Digite uma frase a ser cifrada: ")
key = int(input("Digite a rotacao da cifra: "))

splited_string = string.split()

encrypted_word = {}

for word in splited_string:
    encrypted_word[word] = rotate_word(word, key)

result = ''

for key, value in encrypted_word.items():
    result += key + " "

print(result)

result = '\n'

for key, value in encrypted_word.items():
    result += value + " "

print(result)
