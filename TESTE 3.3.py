classificacao = {
    "Lavínia": 1,
    "Pablo": 2,
    "Amanda": 3,
    "Márcio": 4,
    "Luiz": 5,
    "Manuela": 6,
    "Jorge": 7,
    "Yasmin": 8,
    "Adriano": 9,
    "Matheus": 10
}
nome = input("Qual o seu nome?\n")
if nome in classificacao:
    print(f"Sua posição é a {classificacao[nome]}°")
else:
    print("Você não faz parte dessa classificação")