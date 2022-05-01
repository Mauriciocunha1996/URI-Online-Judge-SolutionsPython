a, b, c, d = input('').split(" ")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if a < c:
    a = int(a) * 60
    c = int(c) * 60
    soma = abs((a+b) - (c+d))
    coverter_hora = soma//60
    converter_minuto = soma % 60
    print(f'O JOGO DUROU {coverter_hora} HORA(S) E {converter_minuto} MINUTO(S)')
if a >= c:
    conv_1 = (24-a) + c
    a = int(a) * 60
    c = int(c) * 60
    soma1 = abs((a + b) - (c + d))
    conv_m = soma1 % 60
    print(f'O JOGO DUROU {conv_1} HORA(S) E {conv_m} MINUTO(S)')



