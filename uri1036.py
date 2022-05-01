from math import pow, sqrt
a, b, c = input('').split(" ")
a = float(a)
b = float(b)
c = float(c)
delta = (pow(b, 2.0)) - 4.0 * a * c
if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    x1 = (-b + (sqrt(delta))) / (2.0 * a)
    x2 = (-b - (sqrt(delta))) / (2.0 * a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
