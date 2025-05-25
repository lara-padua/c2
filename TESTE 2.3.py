def operações(x,y):
    operação= int(input ("Qual operação você quer fazer?\nSoma(1)\nSubtração(2)\nMultiplicação(3)\nDivisão(4)\n"))
    if operação == 1:
        print(x+y)
        z = x+y
    if operação == 2:
        print(x-y)
        z= x-y
    if operação == 3:
        print(x*y)
        z = x*y
    if operação == 4:
        print(x/y)
        z = x/y
    return z

def operações_2(z):
    c = float(input("Escolha um terceiro valor\n"))
    operação= int(input ("Qual operação você quer fazer?\nSoma(1)\nSubtração(2)\nMultiplicação(3)\nDivisão(4)\n"))
    if operação == 1:
        print(z+c)
    if operação == 2:
        print(z-c)
    if operação == 3:
        print(z*c)
    if operação == 4:
        print(z/c)
    print("Obrigada por participar!")
   

print ("Vamos fazer alguns cálculos?!\n")
print ("Escolha dois números\n")
x = float(input("Número 1:"))
y = float(input("Nùmero 2:"))
z = operações(x,y)
continuar = int (input("Deseja continuar?\nSim (1)\nNão(2)\n"))
if continuar == 1:
    operações_2(z)   
if continuar == 2:
    print("Obrigada por participar!")

