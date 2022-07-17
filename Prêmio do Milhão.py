a = int(input())
vezes = 1
acessos = 0
for i in range(0, a):
    n = int(input())
    acessos += n
    if acessos < 1000000:
        vezes+=1
print(vezes)
