n = int(input())
lista = []
vezes = 0
for i in range(1, n+1):
    if n % i == 0:
        lista+=[i]
        vezes += 1
for j in range(0, vezes):
    print(f'{lista[j]}', end=' ')
