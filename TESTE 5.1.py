def calcular_a_media(n1, n2, n3):
    media = (n1+n2+n3)/3
    return media

n1 = float(input("Digite a primeira nota:\n"))
n2 = float(input("Digite a segunda nota:\n"))
n3 = float(input("Digite a terceira nota:\n"))
media = calcular_a_media(n1, n2, n3)

print("A média é:", media)