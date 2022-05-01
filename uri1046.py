h1, h2 = input('').split(" ")
h1 = int(h1)
h2 = int(h2)
cont = 0
cont2 = 0
if h1 > h2 or h1 == h2:
    for c in range(h1+1, h2+1, -1):
        cont += 1
    print(f'O JOGO DUROU {24 - cont} HORA(S)')
elif h2 > h1:
    for c2 in range(h1, h2):
        cont2 += 1
    print(f'O JOGO DUROU {cont2} HORA(S)')
