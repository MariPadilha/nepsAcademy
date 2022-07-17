n = input()
a, b = input().split(' ')
a = float(a); b = float(b)
if n == 'M':
    print(f'{a*b:.2f}')
if n == 'D':
    print(f'{a/b:.2f}')
