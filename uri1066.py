cont = 0
cont1 = 0
cont2 = 0
cont3 = 0
for c in range(1, 6):
    n = int(input(''))
    if n % 2 == 0:
        cont += 1
    if n % 2 != 0:
        cont1 += 1
    if n > 0:
        cont2 += 1
    if n < 0:
        cont3 += 1
print(f'{cont} valor(es) par(es)')
print(f'{cont1} valor(es) impar(es)')
print(f'{cont2} valor(es) positivo(s)')
print(f'{cont3} valor(es) negativo(s)')
