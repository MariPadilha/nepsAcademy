n = int(input())
msg = input()
k = msg.replace(" ", "")
j = len(k)
if j > n:
    print('Mensagem ignorada')
if j <= n:
    print('Mensagem lida')
