notas_p1 = {
    "Ana": 7.5,
    "Bruno": 6.8,
    "Carlos": 9.2,
    "Daniela": 8.1,
    "Eduardo": 5.6,
    "Lara": 7.0,
    "Gabriel": 4.8,
    "Helena": 6.5,
    "Igor": 9.0,
    "Juliana": 8.7,
    "Clara": 7.3,
    "Lucas": 5.9,
    "Mariana": 6.0,
    "Nicolas": 8.0,
    "Olivia": 9.5,
    "Arthur": 4.2,
    "Renata": 7.9,
    "Samuel": 6.6,
    "Thiago": 8.4,
    "Vanessa": 7.2
}

nome = input("Digite o nome do aluno:\n")

if nome in notas_p1:
    print(f"A nota de {nome} na P1 é: {notas_p1[nome]}")
else:
    print("Aluno não encontrado.")