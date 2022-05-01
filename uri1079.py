case = int(input(''))
cont = 1
while cont <= case:
    notas = input('').split(" ")
    n1, n2, n3 = notas  # notas divididas
    cont += 1
    print('{:.1f}'.format((float(n1) * 2 + float(n2) * 3 + float(n3) * 5) / 10))



