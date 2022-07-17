total, per = input().split(' ')
total = int(total);per = int(per)
print(f'{(100-(per*100/total)):.2f}%')
