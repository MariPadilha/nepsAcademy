n = int(input())
dario = xerxes = 0
for i in range(0,n):
    d,x = input().split(' ')
    if d == '0' and x == '1' or d == '0' and x == '1' or d == '0' and x == '2' or d == '1' and x == '2' or d == '1' and x == '3' or d == '2' and x == '3' or d == '2' and x == '4' or d == '3' and x == '0' or d == '3' and x == '4' or d == '4' and x == '1' or d == '4' and x == '0':
        dario +=1
    else:
        xerxes +=1
print('dario') if dario>xerxes else print('xerxes')
