atual, fases = input().split()
atual=int(atual);fases=int(fases)
pontos = input().split(' ')
for i in range(0, fases):
    atual += int(pontos[i])
    if atual > 100:
        atual = 100
    if atual < 0:
        atual = 0
print(atual)
