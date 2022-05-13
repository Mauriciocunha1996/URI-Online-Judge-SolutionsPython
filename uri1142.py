N = int(input(''))
limite = N * 4
cont = 0
for i in range(1, limite):
    cont += 1
    if i % 3 == 0:
        print(f'{i} PUM', sep='\n')
    else:
        print(i, end=' ')

