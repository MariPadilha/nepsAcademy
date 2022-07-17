a, b, c = input().split(' ')
if a == b and b == c:
    print('*')
if a == b and c != a:
    print('C')
if b == c and a != c:
    print('A')
if a == c and b != c:
    print('B')
