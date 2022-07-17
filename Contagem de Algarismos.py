n = int(input())
n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = n0 = 0
for i in range(0, n):
    k = input()
    n1 += k.count('1'); n2 += k.count('2'); n3 += k.count('3')
    n4 += k.count('4'); n5 += k.count('5'); n6 += k.count('6')
    n7 += k.count('7'); n8 += k.count('8'); n9 += k.count('9'); n0 += k.count('0')
print(f'''0 - {n0}
1 - {n1}
2 - {n2}
3 - {n3}
4 - {n4}
5 - {n5}
6 - {n6}
7 - {n7}
8 - {n8}
9 - {n9}''')
