n = int(input(''))
for c in range(0, n):
    num = int(input(''))
    mult = 0
    for cont in range(2, num):
        if num % cont == 0:
            mult += 1
    if mult == 0:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')

