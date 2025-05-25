vetor = list(map(float, input("Digite os elementos do vetor separados por espaço:\n").split()))
escalar = float(input("Digite o escalar:\n"))

resultado = [x * escalar for x in vetor]

print("Resultado da multiplicação:", resultado)