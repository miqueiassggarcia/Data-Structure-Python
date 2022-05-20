def rotate_word(word, key):
    new_word = ""
    for letter in word:
        letter_tmp = ord(letter) + key
        if letter_tmp > ord("z"):
            letter_tmp -= 26
        elif letter_tmp < ord("a"):
            letter_tmp += 26
        new_word += chr(letter_tmp)
    return new_word

def generate_dictionary(address):
    file = open(address, "r")
    list_of_words = file.read().lower().split()

    dictionary = {}
    for word in list_of_words:
        dictionary[word] = None

    return dictionary

def verify_cipher_compatibility(word, dictionary):
    for i in range(1, 14):
        encrypt_word = rotate_word(word, i)
        if encrypt_word in dictionary:
            print(word, i, encrypt_word)

dictionary = generate_dictionary("words.txt")

for word in dictionary.keys():
    verify_cipher_compatibility(word, dictionary)
