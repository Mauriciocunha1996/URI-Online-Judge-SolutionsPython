soma = 0
cont = 0
while True:
    n = int(input())
    if n > 0:
        soma += n
        cont += 1
    if n < 0:
        break
media = soma / cont
print(f'{media:.2f}')

