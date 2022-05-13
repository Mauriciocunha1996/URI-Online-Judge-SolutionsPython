while True:
    x = int(input())
    cont = 0
    if x != 0:
        for i in range(1, x + 1):
            cont += 1
            if cont == x:
                print(i, sep='\n')
            else:
                print(i, end=' ')
    else:
        break
