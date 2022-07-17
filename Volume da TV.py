total, n = input().split(' ')
a = input().split(' ')
total = int(total);n = int(n)
for i in range(0, n):
    total += int(a[i])
    if total > 100:
        total = 100
    if total < 0:
        total = 0
print(total)
