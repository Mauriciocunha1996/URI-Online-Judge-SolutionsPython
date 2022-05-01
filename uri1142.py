N = int(input(''))

cont = 0
while cont < N:
    cont += 1
    print(f'{cont} PUM\n' if cont % 3 == 0 else f'{cont}', end=' ')

