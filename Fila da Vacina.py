a = int(input())
if a%3!=0:
    for i in range(3, a,6):
        print(i)
else:
    for i in range(3, a+1,3):
        print(i)
