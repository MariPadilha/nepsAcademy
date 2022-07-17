n = int(input())
lista = []
lista += input().split(' ')
a = 0
b = 0
for i in range(0, n):
    f = lista[i]
    f = int(f)
    if f == 1 and a == 0:
        a = 1
    elif f == 1 and a == 1:
        a = 0
    if f == 2 and b == 0 and a == 0:
        b = 1
        a = 1
    elif f == 2 and b == 1 and a == 0:
        b = 0
        a = 1
    elif f == 2 and b == 0 and a == 1:
        b = 1
        a = 0
    elif f == 2 and b == 1 and a == 1:
        b = 0
        a = 0
print(a)
print(b)
