a1, a2 = input().split(' ');b1, b2 = input().split(' ')
a1 = int(a1);a2 = int(a2);b1 = int(b1);b2 = int(b2)
if a1 * a2 == b1 * b2:
    print('Empate')
elif a1 * a2 < b1 * b2:
    print('Segundo')
else:
    print('Primeiro')
