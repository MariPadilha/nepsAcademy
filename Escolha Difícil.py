c, b, p = input().split(' ')
carne, bacon, pato = input().split(' ')
c = int(c)
b = int(b)
p = int(p)
carne = int(carne)
bacon = int(bacon)
pato = int(pato)
falta = 0
if c < carne:
	falta += carne - c
if b < bacon:
	falta += bacon - b
if p < pato:
	falta += pato - p
print(falta)
