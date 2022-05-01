from math import fabs, pow
from statistics import median
A, B, C = input('').split(" ")
A = float(A)
B = float(B)
C = float(C)
lista = [A, B, C]
a = max(lista, key=float)
b = min(lista, key=float)
c = median(lista)
if fabs(b - c) < a < b + c and fabs(c - a) < b < c + a and fabs(a - b) < c < a + b:
    if pow(a, 2) == (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO RETANGULO')
    if pow(a, 2) > (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO OBTUSANGULO')
    if pow(a, 2) < (pow(b, 2) + pow(c, 2)):
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    if a == b and b != c or b == c and b != a or c == a and c != b or c == b and c != a:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
