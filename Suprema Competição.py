n = int(input())
will = eleven = 0
for i in range(0, n):
    a, b = input().split(' ')
    if a == '0' and b == '2' or a == '0' and b == '1' or a == '1' and b == '2' or a == '1' and b == '3' or a == '2' and b == '3' or a == '2' and b == '4' or a == '3' and b == '0' or a == '3' and b == '4' or a == '4' and b == '0' or a == '4' and b == '1':
        will += 1
    else:
        eleven += 1
print('will') if will > eleven else print('11')
