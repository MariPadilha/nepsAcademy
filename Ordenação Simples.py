n = int(input())
a = input().split(' ')
lista = []
for i in range(0, n):
    h = a[i]
    h = int(h)
    lista += [h]
lista.sort()
for j in range(0, n):
    print(f'{lista[j]}', end=' ')
