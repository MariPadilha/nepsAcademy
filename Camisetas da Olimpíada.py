n = int(input())
camisetas = input()
p = camisetas.count('1'); m = camisetas.count('2')
pequeno = int(input()); medio = int(input())
if pequeno == p and medio == m:
    print('S')
else:
    print('N')
