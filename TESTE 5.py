print("Vamos trabalhar com triângulos!")
x = float(input("Digite o tamanho do primeiro lado do triângulo:"))
y = float(input("Digite o tamanho do segundo lado do triângulo:"))
z = float(input("Digite o tamanho do terceiro lado do triângulo:"))
if x == y == z:
    print("Isso é um triângulo equilátero!")
elif x == y != z or y == z != x or z == x != y:
    print("Isso é um triângulo isóceles!")
else:
    print("Isso é um triângulo escaleno!")