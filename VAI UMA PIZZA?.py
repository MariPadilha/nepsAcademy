n = int(input())
print(int(n/8)) if n % 8 == 0 else print(int((n-(n%8))/8+1))
