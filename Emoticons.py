a = input()
feliz = triste = 0
feliz += a.count(':-)'); triste += a.count(':-(')
if feliz == triste:
    print('neutro')
elif feliz > triste:
    print('divertido')
else:
    print('chateado')
