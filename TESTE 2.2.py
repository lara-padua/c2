x = int(input("Escolha um número inteiro:\n"))
print ("Os números primos dessa sequência são:\n")
while x > 0:
    divisores = 0
    for i in range(1, x+1):
        if x % i == 0:
            divisores += 1

    if divisores == 2:
        print(x)
    x -= 1
