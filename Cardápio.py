menu = 0
n = int(input()); vezes = int(input())
if n == 1:
    menu = 6.90
if n == 2:
    menu = 7.30
if n == 3:
    menu = 4.50
if n == 4:
    menu = 5.70
print(f'O valor total da compra e R$ {(menu*vezes):.2f}')
