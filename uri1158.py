n = int(input(''))
for c in range(0, n):
    x, y = input('').split(" ") # pega dois valores na mesma linha e atribui as variávies
    # converte as variáveis
    x = int(x)
    y = int(y)
    limitador = 1
    soma = 0
    while limitador <= y:
        if x % 2 != 0:
            soma += x
            x += 1
            limitador += 1
        if x % 2 == 0:
            x += 1
    print(soma)

"""def numero(n):
    cont = 0
    while cont < n:
        x, y = input('').split(" ")
        x = int(x)
        y = int(y)
        cont += 1
        lista = []
        for c in range(x, x*y):
            if c % 2 != 0:
                lista.append(c)
        print(sum(lista[:y]))


n = int(input(''))
numero(n)"""





