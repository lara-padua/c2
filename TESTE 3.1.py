lista = [1, 7, 14, 15, 19, 24, 32, 56]

def soma_lista(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + soma_lista(l[1:])

resultado = soma_lista(lista)
print("A soma é:", resultado)