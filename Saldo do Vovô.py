n, saldo = input().split(' ')
n = int(n); saldo = int(saldo)
final = saldo
for i in range(0, n):
    num = int(input())
    saldo += num
    if saldo < final:
        final = saldo
print(final)
