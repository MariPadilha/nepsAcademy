a1, a2, a3, a4, a5 = input().split()
a1 = float(a1); a2 = float(a2); a3 = float(a3); a4 = float(a4); a5 = float(a5)
a = (a1+a2+a3+a4+a5)-min(a1,a2,a3,a4,a5)-max(a1,a2,a3,a4,a5)
print(f'{a:.1f}')
