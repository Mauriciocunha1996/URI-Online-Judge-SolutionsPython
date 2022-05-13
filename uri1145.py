coluna, linha = input('').split(' ')
linha = int(linha)
coluna = int(coluna)
cont = 0
for i in range(1, linha + 1):
    if i % coluna == 0:
        print(i, sep='\n')
    else:
        print(i, end=' ')
