cont = 0
soma = 0.0
for c in range(1, 7):
    n = float(input(''))
    if n > 0.0:
        cont += 1
        soma += n

print(f'{cont} valores positivos')
print(f'{soma/cont:.1f}')

