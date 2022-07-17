a = int(input())
ano = int(input())
if 2020 - ano >= 18:
    print(2020-ano)
    print('Pode tirar carteira')
    print((2020 - ano)-18)
else:
    print(2020 - ano)
    print('Nao pode tirar carteira')
    print(18-(2020 - ano))
