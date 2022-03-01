n = int(input())
moedas = 0
valor100 = n // 100
if valor100 > 0:
    moedas += valor100
n = n - valor100 * 100
valor50 = n // 50
if valor50 > 0:
    moedas += valor50
n = n - valor50 * 50
valor25 = n // 25
if valor25 > 0:
    moedas += valor25
n = n - valor25 * 25
valor10 = n // 10
if valor10 > 0:
    moedas += valor10
n = n - valor10 * 10
valor5 = n // 5
if valor5 > 0:
    moedas += valor5
n = n - valor5 * 5
valor1 = n // 1
if valor1 > 0:
    moedas += valor1
n = n - valor1 * 1
print(f'''{moedas}
{valor100}
{valor50}
{valor25}
{valor10}
{valor5}
{valor1}''')
