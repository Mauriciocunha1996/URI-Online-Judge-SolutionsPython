notas = []
while True:
    n = float(input(''))
    if 0 <= n <= 10:
        notas.append(n)
        if len(notas) == 2:
            media = sum(notas)/(len(notas))
            print(f'media = {media}')
    else:
        print('nota invalida')

