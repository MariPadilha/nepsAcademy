a,b,c,d = input().split(' ')
a = int(a);b = int(b); c = int(c);d = int(d)
lista = [a, b, c, d]
lista.remove(max(a,b,c,d))
lista.remove(min(a,b,c,d))
v1 = max(a,b,c,d) + min(a,b,c,d)
v2 = lista[0] + lista[1]
print(max(v1,v2)-min(v1,v2))
