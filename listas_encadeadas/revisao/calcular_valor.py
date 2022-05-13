def calcularValorAluguel():
    quantidadeKm = int(input("Digite a quantidade de quilometros percorridos: "))
    quantidadeDeDias = int(input("Digite a quantidade de dias de aluguel: "))

    return quantidadeKm * 0.15 + quantidadeDeDias * 60

print("O valor total do aluguel é ", calcularValorAluguel())
