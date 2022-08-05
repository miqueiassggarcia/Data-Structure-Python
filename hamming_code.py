import random
from functools import reduce
import operator as op

bits = []
for i in range(16):
    bits.append(random.randint(0, 1))

lista = list(enumerate(bits))

print(lista)

separateList = [i for i, bit in enumerate(bits) if bit]

print(separateList)

resultOfList = reduce(op.xor, [i for i, bit in enumerate(bits) if bit])

print(resultOfList)
print(bin(resultOfList))

bits[8] = not bits[8]
bits[1] = not bits[1]

newResultOfList = reduce(lambda x, y: x ^y, [i for i, bit in enumerate(bits) if bit])

print(newResultOfList)

def hamming_syndrome(bits):
    return reduce(
        lambda x, y: x ^ y,
        [i for (i, b) in enumerate(bits) if b]
    )