n = input();lista = [];a = '';b=''
for i in range(0, len(n)):
    if n[i] == 'a' or n[i] == 'e' or n[i] == 'i' or n[i] =='o' or n[i] =='u':
        lista+=[n[i]]
for k in range(0, len(lista)):
    a += lista[k]
lista.reverse()
for p in range(0, len(lista)):
    b += lista[p]
if a == b:
    print('S')
else:
    print('N')
