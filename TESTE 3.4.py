gabarito = ["a", "c", "b", "b", "e", "e", "d", "a", "a", "b"]
respostas_aluno = [""]*10 
print ("Insira as suas respostas!")
respostas_aluno [0] = input("Primeira questão:")
respostas_aluno [1] = input("Segunda questão:")
respostas_aluno [2] = input("Terceira questão:")
respostas_aluno [3] = input("Quarta questão:")
respostas_aluno [4] = input("Quinta questão:")
respostas_aluno [5] = input("Sexta questão:")
respostas_aluno [6] = input("Sétima questao:")
respostas_aluno [7] = input("Oitava questão:")
respostas_aluno [8] = input("Nona questão:")
respostas_aluno [9] = input("Décima questão:")

x = 0
acertos = 0
for x in range(0,10):
    if gabarito[x] == respostas_aluno[x]:
        acertos += 1
    x +=1

if acertos>=5:
    print(f"Você acertou {acertos} questões da prova, parabéns!")
else:
    print(f"Você acertou {acertos} questões da prova, estude mais para a próxima!")
