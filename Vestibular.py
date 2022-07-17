n = int(input())
gabarito = input()
respostas = input()
pontos = 0
for i in range(0, n):
    if gabarito[i] == respostas[i]:
        pontos += 1
print(pontos)
