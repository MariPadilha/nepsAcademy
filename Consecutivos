n = int(input())
lista = input().split()
soma = 1
li=[]
for i in range(1, n):
    if lista[i] == lista[i-1]:
        soma += 1
    if lista[i] != lista[i-1]:
        li += [soma]
        soma = 1
if max(li) > soma:
    print(max(li))
if max(li) < soma:
    print(soma)
