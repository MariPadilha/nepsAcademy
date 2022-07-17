n = int(input())
soma = 0
divisores = []
qdivi = 0
for i in range(1, n+1):
    if n % i == 0:
        soma += i
        qdivi += 1
        divisores += [i]
print(f'{qdivi} divisor(es):', end='')
for j in range(0, qdivi):
    print(f' {divisores[j]}', end='')
print('')
print(f'Soma de divisores = {soma}')
if qdivi > 2 or qdivi == 1:
    print('Nao primo')
if qdivi == 2:
    print('Primo')
